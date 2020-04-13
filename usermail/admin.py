from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import path

from usermail.tasks import send_email_to_all
from .models import UserProfile


# Register your models here.

@register(UserProfile)
class UserProfileAdmin(UserAdmin):
    change_list_template = 'admin/payout-admin.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('send_mail_to_all/', self.send_mail_to_all, name='send_mail_to_all')
        ]
        return my_urls + urls

    def send_mail_to_all(self, request):
        # self.model.objects.all().update(is_immortal=True)
        send_email_to_all.delay()
        self.message_user(request, "Email has been sent to all.")
        return HttpResponseRedirect("../")
