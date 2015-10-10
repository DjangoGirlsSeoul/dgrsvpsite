from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import requires_csrf_token
from django.core import serializers

from .models import Event, Reservation

def events_list(request):
    events = Event.objects.order_by('-date')

    context = {'events': events}
    return render(request,'rsvp/events_list.html', context)

@requires_csrf_token
def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    rsvp = []
    if request.user:
        rsvp = Reservation.objects.filter(event=event, user=request.user)
    print(rsvp)
    print(rsvp[0].attending)
    context = {'event': event, 'rsvp': rsvp}
    return render(request,'rsvp/event_detail.html', context)

@require_http_methods(["POST"])
def event_signup(request, event_id):
    user = request.user
    event = get_object_or_404(Event, id=event_id)
    rsvp = Reservation.objects.filter(event=event, user=user)
    if rsvp:
        rsvp[0].attending = not rsvp[0].attending
        rsvp[0].save()
    else:
        rsvp = Reservation(event=event, user=user, attending=True)
        rsvp.save()
    rsvp_json = serializers.serialize('json', rsvp)
    return HttpResponse(rsvp_json, content_type='application/json')