from django.db import models
import json
from donation.models.base import DonationBase
# from donation.models.donation import Donation

class DonationRequest(DonationBase):
    """Represents a request for blood donation."""

    _BUFFER_SCALE = 2  # Buffer scale for calculating donors needed

    # Additional attributes specific to DonationRequest
    patient_name = models.CharField(max_length=100, blank=True, null=True)
    patient_story = models.TextField()
    patient_avatar = models.ImageField(upload_to="patient_avatars", blank=True)
    hospital = models.CharField(max_length=100, blank=True, null=True)
    donors_needed = models.PositiveIntegerField(default=1)
    pending_donations = models.ForeignKey("Donation", on_delete=models.CASCADE, 
                                          null=True, blank=True, 
                                          related_name='pending_requests')
    
    verified_donations = models.ForeignKey("Donation", on_delete=models.CASCADE, 
                                           null=True, blank=True, 
                                           related_name='verified_requests')
    
    
    def set_donors_needed(self, number_of_pints):
        """
        Set the number of donors needed based on the number of pints specified,
        using a buffer scale.
        """
        self.donors_needed = int(self.number_of_pints * self._BUFFER_SCALE)
        self.save()
        
    def add_donation(self, donation):
        """
        Add a blood donation associated with this donation request.
        """
        donation.donation_request = self
        donation.save()

        if donation.status == "Verified":
            self.donors_needed -= 1
            self.save()
    
    def __str__(self):
        return f"Donation Request for {self.patient_name}"

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        return {
            "request_id": self.id,
            "patient_name": self.patient_name,
            "hospital": self.hospital,
            "blood_group": self.blood_group,
            "donors_needed": self.donors_needed,
            "status": self.status,
        }

    def to_json(self):
        """Returns a JSON representation of the model."""
        return json.dumps(self.to_dict())

    class Meta:
        verbose_name_plural = "Donation Requests"