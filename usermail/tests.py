from django.test import TestCase
from mock import patch

from usermail.tasks import send_email_to_emails
from .models import UserProfile


# Create your tests here.

class UserEmailTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create(username="test1", email="testuser1@yopmail.com")
        UserProfile.objects.create(username="test2", email="testuser2@yopmail.com")
        UserProfile.objects.create(username="test3", email="testuser3@yopmail.com")

    def test_user_email(self):
        user_emails = UserProfile.objects.all().values_list('email', flat=True)[::1]
        with patch('usermail.tasks.send_email_to_emails.delay') as mock_task:
            send_email_to_emails.delay(user_emails)
            self.assertTrue(mock_task.called)
