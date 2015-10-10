from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

class Reservation(models.Model):
    notes =  models.TextField()
    event = models.ForeignKey("Event")
    user = models.ForeignKey(User)
    attending = models.BooleanField()
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    date = models.DateTimeField()
    location = models.TextField()
    capacity = models.IntegerField()
    notes =  models.TextField()
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Event, self).save(*args, **kwargs)