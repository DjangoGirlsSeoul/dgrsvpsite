from django.utils import timezone
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import requires_csrf_token,csrf_exempt
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

from .models import Event, Reservation
from django.core.mail import EmailMessage

def events_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request,'rsvp/events_list.html', context)

@requires_csrf_token
def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    rsvp = []
    rsvplist = []
    if request.user.is_authenticated():
        rsvp = Reservation.objects.filter(event=event, user=request.user)
        rsvplist = Reservation.objects.filter(event=event, attending=True)
        print("total rsvp:",len(rsvplist))
    number_attending = Reservation.objects.filter(event=event, attending=True).count()

    context = {'event': event, 'rsvp': rsvp, 'number_attending': number_attending, 'spaces_left': event.capacity - number_attending, 'rsvplist': rsvplist}
    return render(request,'rsvp/event_detail.html', context)

@require_http_methods(["POST"])
@login_required
def event_signup(request, event_id):
    user = request.user
    if not user.is_authenticated():
        raise PermissionDenied
    event = get_object_or_404(Event, id=event_id)
    rsvp = Reservation.objects.filter(event=event, user=user)
    print("event_signup",len(rsvp))
    if rsvp:
        rsvp_single = rsvp.first()
        rsvp_single.attending = not rsvp_single.attending
        rsvp_single.save()
        print(user.email)
        email = EmailMessage('Hi!', 'Cool message for %recipient.first_name%', 'seoul@djangogirls.org', [user.email])
        email.extra_headers['recipient_variables'] = '{'+ str(user.email) +':{"first_name":'+ str(user.first_name) + '}}'
        print(user.first_name)
        email.send()
        print ("sent_email")
    else:
        rsvp = Reservation(event=event, user=user, attending=True)
        rsvp.save()
        mail = EmailMessage('Hi!', 'Cool message for %recipient.first_name%', 'seoul@djangogirls.org', [user.email])
        email.extra_headers['recipient_variables'] = '{'+ str(user.email) +':{"first_name":user.first_name}}'
        email.send()
        rsvp = [rsvp]
    rsvp_json = serializers.serialize('json', rsvp)
    return HttpResponse(rsvp_json, content_type='application/json')

def user_rsvplist(request):
    rsvps = Reservation.objects.filter(user=request.user)
    print(len(rsvps))
    context = {'rsvps': rsvps}
    return render(request,'rsvp/user_rsvp.html', context)

