
from django.db import models
from django.utils import timezone
from donation.models.base import DonationBase
from django.contrib.auth.models import User
# from .donationrequest import DonationRequest


class Donation(DonationBase):
    _CONVERSION_RATE = 3
    donor_name = models.CharField(max_length=100, blank=True, null=True)
    donor_phone = models.CharField(max_length=20, blank=True, null=True)
    donor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    donation_request = models.ForeignKey("DonationRequest", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=DonationBase.STATUS_CHOICES, default="Pending")

    scheduled_date = models.DateTimeField(blank=True, null=True)
    donation_request = models.ForeignKey("DonationRequest", on_delete=models.SET_NULL, null=True, blank=True)

    # Fields related to verification
    verification_date = models.DateTimeField(blank=True, null=True)
    verification_photo = models.ImageField(upload_to="donor_photos", blank=True, null=True)

    potential_lives_saved = models.PositiveIntegerField(default=0)
    
    

    def calculate_lives_saved(self):
        self.potential_lives_saved = int(self.number_of_bags * self._CONVERSION_RATE)
        self.save()

    def schedule_donation(self, scheduled_date):
        if self.is_pending():
            self.scheduled_date = scheduled_date
            self.save()

    def complete_donation(self):
        if self.is_pending() and self.scheduled_date:
            self.set_status("Completed")
            self.is_completed = True
            self.donation_date = self.scheduled_date
            self.verification_date = None  # Reset verification date
            self.save()

    def update_verification(self, donor_photo, blood_bag_photo):
        if self.is_completed():
            self.verification_date = timezone.now()
            self.donor_photo = donor_photo
            self.blood_bag_photo = blood_bag_photo
            self.save()

    def __str__(self):
        """Returns a string representation of the model."""
        if self.is_pending():
            return f"Donation by {self.donor_name} scheduled on {self.scheduled_date}"
        elif self.status == "Completed":
            return f"Donation by {self.donor_name} completed on {self.donation_date} pending verification"
        return f"Donation by {self.donor_name}, {self.status}"

    class Meta:
        verbose_name_plural = "Blood Donations"
