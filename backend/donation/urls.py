# donation/urls.py
from django.urls import path
from . import views


app_name = 'donation'

urlpatterns = [
    #donation app-specific URL patterns here
    path('create_request/', views.create_request, name='create_request'),
    path('list_requests/', views.request_list, name='request_list')
]