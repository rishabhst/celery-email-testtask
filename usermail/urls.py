from django.urls import path
from . import views

urlpatterns = [
    path('http_response/', views.http_response, name='http_response'),
    path('send_mail/', views.send_mail, name='send_mail')
]