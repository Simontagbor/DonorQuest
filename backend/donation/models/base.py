from django.db import models
from django.utils import timezone
import uuid

class BaseModel(models.Model):
    """Abstract base model for all models in the project."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class DonationBase(BaseModel):
    """Abstract base class for Donation and DonationRequest models."""

    # Choices for blood group, donation option, donation type, and status
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Stale", "Stale"),
        ("Listed", "Listed"),
        ("Completed", "Completed"),
        ("Canceled", "Canceled"),
        ("Rejected", "Rejected"),
        ("Verified", "Verified")
    ]
    DONATION_OPTIONS = [
        ('replacement', 'Replacement'),
        ('voluntary', 'Voluntary'),
    ]
    DONATION_TYPES = [
        ('regular', 'Regular'),
        ('platelets', 'Platelets'),
        ('plasma', 'Plasma'),
        ('double_red_cells', 'Double Red Cells'),
    ]

    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES, max_length=3, default="A+")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    donation_option = models.CharField(max_length=20, choices=DONATION_OPTIONS, default="Voluntary")
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES, default="Regular")
    number_of_pints = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.PositiveIntegerField(default=18)

    def set_status(self, status):
        """Sets the status of the donation."""
        self.status = status
        self.save()
        
    def is_pending(self):
        """Returns True if the donation is pending."""
        if self.status == "Pending":
            return True
        return False

    def is_completed(self):
        """Returns True if the donation is completed."""
        if self.status == "Completed":
            return True
        return False
    def is_verified(self):
        """Returns True if the donation is verified."""
        if self.status == "Verified":
            return True
        return False

    class Meta:
        abstract = True