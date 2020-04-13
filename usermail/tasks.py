from __future__ import absolute_import, unicode_literals

from celery import shared_task

from usermail.models import UserProfile
from usermail.utils.email_helper import send_mail_using_post_office


@shared_task
def send_email_to_all():
    user_emails = UserProfile.objects.all().values_list('email', flat=True)
    for email in user_emails:
        send_mail_using_post_office(email, 'Hello There!', 'How are you!')
