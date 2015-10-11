from datetime import timedelta

from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User 

from .models import Event, Reservation

class ReserveEvent(TestCase):
    def setUp(self):
        self.client = Client()
        u = User.objects.create_user('test_user', 'test@example.com', 'password1')
        u.save()
        event = Event(id=10, title="test_event", start_time=timezone.now(), duration=timedelta(), location="123 fake street", capacity=30, notes="this is a test note")
        event.save()

    def test_not_allowed_reserve_event(self):
        """
        User is not logged in so not allowed to RSVP for anything
        """
        response = self.client.post('/rsvp/event_signup/10/', {}, follow=True)
        self.assertEqual(response.status_code, 403)

    def test_reserve_event(self):
        self.client.login(username="test_user", password="password1")
        self.client.post('/rsvp/event_signup/10/', {}, follow=True)
        user = User.objects.get(username="test_user")
        r = Reservation.objects.filter(event_id=10, user=user)
        self.assertEqual(r.first().user.username, "test_user")
        self.assertEqual(r.first().attending, True)

    def test_unreserve_event(self):
        self.client.login(username="test_user", password="password1")
        user = User.objects.get(username="test_user")
        event = Event.objects.get(id=10)
        r = Reservation(event=event, user=user, attending=True)
        r.save()
        r = Reservation.objects.filter(event_id=10, user=user)
        self.assertEqual(r.first().user.username, "test_user")
        self.assertEqual(r.first().attending, False)
