from django.utils import timezone
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import requires_csrf_token
from django.core import serializers

from .models import Event, Reservation

def events_list(request):
    upcoming_events = Event.objects.filter(start_time__gte=timezone.now())
    past_events = Event.objects.filter(start_time__lte=timezone.now())

    context = {'upcoming_events': upcoming_events, 'past_events': past_events}
    return render(request,'rsvp/events_list.html', context)

@requires_csrf_token
def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    rsvp = []
    if request.user:
        rsvp = Reservation.objects.filter(event=event, user=request.user)
    number_attending = Reservation.objects.filter(event=event, attending=True).count()
    context = {'event': event, 'rsvp': rsvp, 'number_attending': number_attending, 'spaces_left': event.capacity - number_attending}
    return render(request,'rsvp/event_detail.html', context)

@require_http_methods(["POST"])
def event_signup(request, event_id):
    user = request.user
    event = get_object_or_404(Event, id=event_id)
    rsvp = Reservation.objects.get(event=event, user=user)
    if rsvp:
        rsvp.attending = not rsvp.attending
        rsvp.save()
    else:
        rsvp = Reservation(event=event, user=user, attending=True)
        rsvp.save()
    rsvp_json = serializers.serialize('json', [rsvp])
    return HttpResponse(rsvp_json, content_type='application/json')
