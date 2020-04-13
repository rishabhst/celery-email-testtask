from __future__ import absolute_import, unicode_literals

from celery import shared_task

from usermail.models import UserProfile


@shared_task
def send_email_to_all():
    user_mails = UserProfile.objects.all().values_list('email', flat=True)
    print(user_emails)
    print("-------------------------------------")
