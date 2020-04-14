from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import path

from usermail.tasks import send_email_to_emails
from .models import UserProfile


@register(UserProfile)
class UserProfileAdmin(UserAdmin):
    change_list_template = 'admin/payout-admin.html'
    actions = ['send_mail_to_selected_user']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('send_mail_to_all/', self.send_mail_to_all,
                 name='send_mail_to_all'),
        ]
        return my_urls + urls

    def send_mail_to_all(self, request):
        """
        This task can also performed by below action, but we have created it to show that we can customise
        django-admin page as per our need.
        """
        user_emails = UserProfile.objects.filter(is_staff=False).values_list('email', flat=True)[::1]
        send_email_to_emails.delay(user_emails)
        self.message_user(request, "Email has been sent to all.")
        return HttpResponseRedirect("../")

    def send_mail_to_selected_user(self, request, queryset):
        """
        Using this action, we can send email to selected users. Admin can select one or all users from the list.
        """
        user_emails = queryset.values_list('email', flat=True)[::1]
        send_email_to_emails.delay(user_emails)
        self.message_user(request, "Email has been sent to selected users.")

    send_mail_to_selected_user.short_description = "Sent email to selected users"
