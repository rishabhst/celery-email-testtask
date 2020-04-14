from __future__ import absolute_import, unicode_literals
from celery import shared_task
from usermail.models import UserProfile
from usermail.utils.email_helper import send_mail_using_post_office


@shared_task
def send_email_to_emails(user_emails):
    print(user_emails)
    for email in user_emails:
        send_mail_using_post_office(
            email, 'A test content', 'This is a test email.')
