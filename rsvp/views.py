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
from django.core.mail import EmailMessage,EmailMultiAlternatives
import json
from django.template import Context
from django.template.loader import render_to_string, get_template

EVENT_BASE_URL = "http://www.djangogirlsseoul.org/rsvp/{}/"
FROM_EMAIL = "seoul+events@djangogirls.org"
EMAIL_SUBJECT = "Weekly Study Meetup - {}"

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
    emails = []
    variables = {}
    nameDict = {}
    context = {}
    context["name"] = user.first_name
    emails.append(user.email)
    nameDict["first_name"] = user.first_name
    variables[user.email] = nameDict
    variables = json.dumps(variables)
    if rsvp:
        rsvp_single = rsvp.first()
        rsvp_single.attending = not rsvp_single.attending
        rsvp_single.save()
        context["event_title"] = rsvp_single.event.title
        context["event_location"] = rsvp_single.event.location
        context["event_datetime"] = rsvp_single.event.start_time
        context["event_url"] = EVENT_BASE_URL.format(str(rsvp_single.event.slug))
        message = get_template('rsvp/email_template.html').render(Context(context))
        if rsvp_single.attending :
            email = EmailMultiAlternatives(EMAIL_SUBJECT.format(str(rsvp_single.event.title)), '' , FROM_EMAIL, emails)
            email.attach_alternative(message, "text/html")
        else :
            email = EmailMessage(EMAIL_SUBJECT.format(str(rsvp_single.event.title)), 'Hi %recipient.first_name%,\n\nyou have unrsvped for the event: ' + str(rsvp_single.event.title), FROM_EMAIL, emails)
        email.extra_headers['recipient_variables'] = variables
        email.send()
    else:
        rsvp = Reservation(event=event, user=user, attending=True)
        rsvp.save()
        context["event_title"] = rsvp.event.title
        context["event_location"] = rsvp.event.location
        context["event_datetime"] = rsvp.event.start_time
        context["event_url"] = EVENT_BASE_URL.format(str(rsvp.event.slug))
        message = get_template('rsvp/email_template.html').render(Context(context))
        email = EmailMultiAlternatives(EMAIL_SUBJECT.format(str(rsvp.event.title)), '', FROM_EMAIL, emails)
        email.attach_alternative(message, "text/html")
        email.send()
        rsvp = [rsvp]
    rsvp_json = serializers.serialize('json', rsvp)
    return HttpResponse(rsvp_json, content_type='application/json')

def user_rsvplist(request):
    rsvps = Reservation.objects.filter(user=request.user)
    context = {'rsvps': rsvps}
    return render(request,'rsvp/user_rsvp.html', context)
