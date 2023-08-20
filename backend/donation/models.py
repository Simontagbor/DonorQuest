import uuid
from django.db import models
import json


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserProfile(BaseModel):
    """represents a user profile for DonorQuest"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=5)
    birth_date = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    profile_avatar = models.ImageField(upload_to="profile_avatars", blank=True)

    # TODO add attributes for tracking milestone, Donation History, Badges etc.

    def __str__(self):
        return self.profile_name

    def to_dict(self):
        """returns a dictionary representation of the model"""
        return {
            "user_id": self.id,
            "profile_name": self.profile_name,
            "phone_number": self.phone_number,
            "blood_type": self.blood_type,
            "birth_date": self.birth_date,
            "address": self.address,
            "city": self.city,
            "country": self.country,
        }

    def to_json(self):
        """returns a json representation of the model"""
        return json.dumps(self.to_dict())

    class Meta:
        verbose_name_plural = "User Profiles"


class Donor(UserProfile):
    """represents a donor"""

    DONOR_STATUS = [
        ('scheduled', 'Scheduled'),
        ('donated', 'Donated'),
        ('rejected', 'Rejected'),
        ('missed_appointment', 'Missed Appointment'),
    ]
    donor_name = models.CharField(max_length=50, default="John Doe")
    donor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, choices=DONOR_STATUS, default="scheduled")
   

    def __str__(self):
        return self.donor_name

    def to_dict(self):
        """returns a dictionary representation of the model"""
        return {
            "user_id": self.donor_id,
            "phone_number": self.phone_number,
            "blood_type": self.blood_type,
            "birth_date": self.birth_date,
            "address": self.address,
            "status": self.status,
            "city": self.city,
            "country": self.country,
        }

    def to_json(self):
        """
        returns a json representation of the model
        """
        return json.dumps(self.to_dict())

    class Meta:
        verbose_name_plural = "Donors"

class BloodDonation(BaseModel):
    """Represents a blood donation"""

    DONATION_TYPES = [
        ('regular', 'Regular'),
        ('platelets', 'Platelets'),
        ('plasma', 'Plasma'),
        ('double_red_cells', 'Double Red Cells'),
    ]
    DONATION_OPTIONS= [
        ('replacement', 'Replacement'),
        ('voluntary', 'Voluntary'),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]
    donation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # ForeignKey to Donor model (assume Donor model is defined elsewhere)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=5)
    donation_date = models.DateTimeField(auto_now_add=True)
    number_of_bags = models.IntegerField()
    donation_option = models.CharField(
        max_length=20, choices=DONATION_OPTIONS, default="Voluntary"
    )
    donation_type = models.CharField(
        max_length=20, choices=DONATION_TYPES, default="Regular"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    # Hide the donation_id and donor_id fields from admin panel
    # Don't show these fields in forms

    def __str__(self):
        return self.blood_type

    def to_dict(self):
        """returns a dictionary representation of the model"""
        return {
            "donation_id": self.donation_id,
            "donor_id": self.donor_id,
            "blood_type": self.blood_type,
            "donation_date": self.donation_date,
            "status": self.status,
        }

    def to_json(self):
        """returns a json representation of the model"""
        return json.dumps(self.to_dict())

    class Meta:
        verbose_name_plural = "Blood Donations"
class Patient(BaseModel):
    """represents a patient"""
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # ForeignKey to Donor model (assume Donor model is defined elsewhere)
    # donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=5)
    patient_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)

    # Hide the patient_id and donor_id fields from admin panel
    # Don't show these fields in forms

    def __str__(self):
        """returns a string representation of the model"""
        return """Patient Name: {} | Hospital Name: {} | Blood Type: {}""".format(
            self.patient_name, self.hospital_name, self.blood_type
        )

    def to_dict(self):
        """returns a dictionary representation of the model"""
        return {
            "patient_id": self.patient_id,
            "patient_name": self.patient_name,
            "hospital_name": self.hospital_name,
            "blood_type": self.blood_type,
        }

    def to_json(self):
        """returns a json representation of the model"""
        return json.dumps(self.to_dict())

    class Meta:
        """represents a patient"""

        verbose_name_plural = "Patients"


class DonationRequest(Patient):
    """represents a request for blood donation"""
    __BUFFER_SCALE = 2
    __INTERESTED_DONOR_IDs = {}
    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ForeignKey to Organizer model (assume Organizer model is defined elsewhere)
    # organizer_id = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    number_of_pints = models.PositiveIntegerField()
    request_date = models.DateTimeField(auto_now_add=True)
    patient_story = models.TextField()
    patient_avatar = models.ImageField(upload_to="patient_avatars", blank=True)
    

    STATUS_CHOICES = [
        ("Listed", "Listed"),
        ("Pending", "Pending"),
        ("Stale", "Stale"),
        ("Completed", "Completed"),
        ("canceled", "Canceled"),
    ]
    TAGS = [
        ('Critical Emergency', 'Critical Emergency'),
        ('Urgent', 'Urgent'),
        ('Normal', 'Normal'),
    ]
    tags = models.CharField(max_length=20, choices=TAGS, default="Normal")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    donors_needed = models.PositiveIntegerField(default=1)
    
    ### TODO consider fixing these section 
    # or move them to the business logic ####

    # calculate number of donors needed based on pints
    def update_donors_needed(self):
        """returns the number of donors needed"""	
        return self.number_of_pints * self.BUFFER_SCALE
   
    # decrement the number of donors needed by 1 if 
    # user gets added to interested_donor_ids

    def decrement_donors_needed(self):
        """decrements the number of donors needed by 1 for each interested donors,
          depending on the staus of each donor's donation status"""
        if self.donors_needed > 0:
            pass
    # update donors needed
    # if self.number_of_pints:
    #     self.donors_needed = self.update_donors_needed()
    
    ### TODO consider fixing these section
    #  or move them to the business logic ####

    # Hide the request_id and organizer_id fields from admin panel
    # Don't show these fields in forms
    def __str__(self):
        return self.patient_name

    def to_dict(self):
        """returns a dictionary representation of the model"""
        return {
            "request_id": self.request_id,
            "patient_name": self.patient_name,
            "hospital_name": self.hospital_name,
            "blood_type": self.blood_type,
            "donors_needed": self.donors_needed,
            "request_date": self.request_date,
            "patient_story": self.patient_story,
            "status": self.status,
            "interested_donor_ids": self.interested_donor_ids,
        }

    def to_json(self):
        """returns a json representation of the model"""
        return json.dumps(self.to_dict())

    class Meta:
        verbose_name_plural = "Donation Requests"

class Organizer(BaseModel):
    """represents organizer of blood donation events"""
    # TODO add appropriate attributes and methods

    class Meta:
        verbose_name_plural = "Organizers"