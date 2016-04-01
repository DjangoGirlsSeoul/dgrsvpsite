from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django_markdown.models import MarkdownField



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
        return super(Event, self).save(*args, **kwargs)

