from django.contrib import admin

from donation.models.donationrequest import DonationRequest
from donation.models.userprofile import UserProfile
from donation.models.donation import Donation
from donation.models.donationtarget import DonationTarget
from donation.models.drive import DonationDrive
from donation.models.driveorganizer import DonationDriveOrganizer
from donation.models.donationplan import DonationPlan
from donation.models.hospital import Hospital


admin.site.register(DonationRequest)
admin.site.register(DonationTarget)
admin.site.register(DonationDrive)
admin.site.register(DonationPlan)
admin.site.register(DonationDriveOrganizer)
admin.site.register(Donation)
admin.site.register(UserProfile)
admin.site.register(Hospital)
