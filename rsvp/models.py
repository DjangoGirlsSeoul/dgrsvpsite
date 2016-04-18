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
# code contribution : https://github.com/sujinleeme/my-python-journey/blob/master/PR4E/yahoo-weatherAPI.py


WEBHOOK_URL = settings.WEBHOOK_URL
payload ={}
EVENT_TEXT = "A new *event(스터디 밋업)* has been added for {} {}일 - {}.\n*Rsvp* here <{}|{}>.\n{}"
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
            s = self.start_time
            weekday_ko = WEEKDAY_KO_ARRAY[s.strftime('%A')]
            event_start_time = s.strftime('%H:%M')
            event_month_day = s.strftime('%e')
            forecast_date = s.strftime("%e %b %Y")
            forecast_str = get_weather("seoul",forecast_date)
            payload["text"] = EVENT_TEXT.format(weekday_ko,event_month_day,event_start_time,EVENT_BASE_URL.format(self.slug) \
                                ,EVENT_BASE_URL.format(self.slug), forecast_str)
            if not settings.DEBUG:
                payload["channel"] = "#weekend-studygroup"
            r  = requests.post(WEBHOOK_URL, data = json.dumps(payload))
        return super(Event, self).save(*args, **kwargs)

def get_weather(city,forecastDate):
    baseurl = 'https://query.yahooapis.com/v1/public/yql'
    yql_query = "SELECT * FROM weather.forecast WHERE woeid IN (SELECT woeid FROM geo.places(1) WHERE text='%s')" % city
    params = {'q': yql_query, 'format': 'json'}
    data = requests.get(baseurl, params=params).json()
    if not data['query']['count']:
        return ''

    try:
        channel = data['query']['results']['channel']
        location = channel['location']
        location_summary = ', '.join((location['city'], location['country'], location['region']))
        condition = channel['item']['condition']
        forecast = channel['item']['forecast']
        weather_forecast_str = "Weather forecast for {} is {} with min/max temp {}C/{}C"
        for fdata in forecast:
            if fdata["date"] == forecastDate:
                return weather_forecast_str.format(forecastDate,fdata["text"],int(celsius(fdata["low"])),int(celsius(fdata["high"])))
                break
        word = condition['text']
        temp = '%sF/%dC' % (condition['temp'], int(celsius(condition['temp'])))
        time = condition['date']

        return '''Current weather in %s: %s, %s (%s)''' % (location_summary, word, temp, time)
    except KeyError:
        return ''

def celsius(fahrenheit):
    '''change Fahrenheit to Celsius'''
    return ((int(fahrenheit) - 32) * 5/9)
