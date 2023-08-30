from django.contrib import admin

# Register your models here.

from django.contrib import admin

from donation.models.donationrequest import DonationRequest
from donation.models.userprofile import UserProfile
from donation.models.donation import Donation
from donation.models.donationtarget import DonationTarget

admin.site.register(DonationRequest)
admin.site.register(DonationTarget)
# admin.site.register(Organizer)
admin.site.register(Donation)
admin.site.register(UserProfile)
