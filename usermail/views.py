from django.shortcuts import render
from usermail.models import UserProfile


from django.shortcuts import render
from django.http import HttpResponse

def http_response(request):
    return HttpResponse("This is a simple response !")


def send_mail(request):
    return HttpResponse("This is a simple response to send mails!")	