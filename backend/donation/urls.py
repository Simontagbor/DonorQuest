# donation/urls.py
from django.urls import path
from . import views


app_name = 'donation'

urlpatterns = [
    #donation app-specific URL patterns here
    path('create_request/', views.create_request, name='create_request'),
    path('list_requests/', views.request_list, name='request_list'),
     # URL for the thank you page
    path('thank-you/', views.ThankYouView.as_view(), name='thank_you'),
   # Define a URL pattern for donating for a specific request
    path('donate/request/<uuid:request_id>/', views.specific_patient_donation_view, name='specific_patient_donation_view'),
    # Define a URL pattern for donating for a random.
    path('donate/request/random/', views.random_donation_view, name='random_donation_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # Logout view
    path('logout/', views.logout_view, name='logout'),
]