from django.contrib import admin

# Register your models here.

from .models import DonationRequest, Donor, Patient,  Organizer,  UserProfile

admin.site.register(DonationRequest)
admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(Organizer)
admin.site.register(UserProfile)
