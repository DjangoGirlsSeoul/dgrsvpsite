from django.utils import timezone
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import requires_csrf_token
from django.core import serializers
from django.core.exceptions import PermissionDenied

from .models import Event, Reservation

def events_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request,'rsvp/events_list.html', context)

@requires_csrf_token
def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    rsvp = []
    if request.user.is_authenticated():
        rsvp = Reservation.objects.filter(event=event, user=request.user)
    number_attending = Reservation.objects.filter(event=event, attending=True).count()
    context = {'event': event, 'rsvp': rsvp, 'number_attending': number_attending, 'spaces_left': event.capacity - number_attending}
    return render(request,'rsvp/event_detail.html', context)

@require_http_methods(["POST"])
def event_signup(request, event_id):
    user = request.user
    if not user.is_authenticated():
        raise PermissionDenied 
    event = get_object_or_404(Event, id=event_id)
    rsvp = Reservation.objects.filter(event=event, user=user)
    if rsvp:
        rsvp_single = rsvp.first()
        rsvp_single.attending = not rsvp_single.attending
        rsvp_single.save()
    else:
        rsvp = Reservation(event=event, user=user, attending=True)
        rsvp.save()
        rsvp = [rsvp]
    rsvp_json = serializers.serialize('json', rsvp)
    return HttpResponse(rsvp_json, content_type='application/json')
