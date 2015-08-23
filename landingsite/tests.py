from django.test import TestCase, Client
from django.core import mail

class ContactUsEmailTest(TestCase):
    def test_contact_us_email(self):
        c = Client()
        c.post("/", {"full_name": "Test Email" ,"email": 'test@example.com', "message": "this is a test message"})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Get in touch - Code For Everyone website')

