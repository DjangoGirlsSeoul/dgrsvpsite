from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods

from .models import Event, Reservation

def events_list(request):
    events = Event.objects.order_by('-date')

    context = {'events': events}
    return render(request,'rsvp/events_list.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)

    context = {'event': event}
    return render(request,'rsvp/event_detail.html', context)

@require_http_methods(["POST"])
def event_signup(request, event_id):
    user = request.user
    if not user:
        return 'something'
    event = get_object_or_404(Event, id=event_id)
    rsvp = Reservation.objects.get(event=event, user=user)
    if rsvp:
        rsvp.attending = not rsvp.attending
    else:
        rsvp = Reservation.create(event=event, user=user, attending=True)
    return JsonResponse(rsvp)