from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    date = models.DateTimeField()
    notes =  models.TextField()
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title  = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.TextField()
    capacity = models.IntegerField()
    notes =  models.TextField()
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title