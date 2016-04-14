from datetime import timedelta,datetime,timezone

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django_markdown.models import MarkdownField
import json
import requests
import time
from datetime import timezone
from django.conf import settings

WEBHOOK_URL = settings.WEBHOOK_URL
payload ={}
EVENT_TEXT = "A new event(스터디 모임) has been added for {}일 {} - {}. Rsvp <{}|here>"
EVENT_BASE_URL = "http://www.djangogirlsseoul.org/rsvp/{}/"
WEEKDAY_KO_ARRAY = {'Monday':'월','Tuesday':'화','Wednesday':'수','Thursday':'목','Friday':'금','Saturday':'토','Sunday':'일'}

class Reservation(models.Model):
    notes =  models.TextField()
    event = models.ForeignKey("Event")
    user = models.ForeignKey(User)
    attending = models.BooleanField(default=False)
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return "{}-{}".format(self.user.username, self.event.title)

class Event(models.Model):
    title  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    start_time = models.DateTimeField()
    duration = models.DurationField(default=timedelta())
    location = models.TextField()
    capacity = models.IntegerField()
    notes =  MarkdownField()
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)


    def end_time(self):
        return self.start_time + self.duration

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            # s = utc_to_local(self.start_time)
            s = self.start_time
            weekday_ko = WEEKDAY_KO_ARRAY[s.strftime('%A')]
            event_start_time = s.strftime('%H:%M')
            event_month_day = s.strftime('%e')
            payload["text"] = EVENT_TEXT.format(event_month_day,weekday_ko,event_start_time,EVENT_BASE_URL.format(self.slug))
            if not settings.DEBUG:
                payload["channel"] = "#weekend-studygroup"
            r  = requests.post(WEBHOOK_URL, data = json.dumps(payload))
        return super(Event, self).save(*args, **kwargs)

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
