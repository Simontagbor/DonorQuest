# import uuid
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# import json

# class CustomUserManager(BaseUserManager):
#     """
#     Custom manager for the CustomUser model.

#     This manager provides methods to create users and superusers.
#     """

#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Create and return a new user with the given email and password.

#         Args:
#             email (str): User's email address.
#             password (str): User's password.
#             extra_fields: Additional fields for the user.

# #         Returns:
# #             CustomUser: Newly created user.
# #         """
# #         if not email:
# #             raise ValueError("Email field must be set")
# #         email = self.normalize_email(email)
# #         user = self.model(email=email, **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user

# #     def create_superuser(self, email, password=None, **extra_fields):
# #         """
# #         Create and return a new superuser with the given email and password.

# #         Args:
# #             email (str): Superuser's email address.
# #             password (str): Superuser's password.
# #             extra_fields: Additional fields for the superuser.

# #         Returns:
# #             CustomUser: Newly created superuser.
# #         """
# #         extra_fields.setdefault("is_staff", True)
# #         extra_fields.setdefault("is_superuser", True)

# #         if extra_fields.get("is_staff") is not True:
# #             raise ValueError("Superuser must have is_staff=True.")
# #         if extra_fields.get("is_superuser") is not True:
# #             raise ValueError("Superuser must have is_superuser=True.")

# #         return self.create_user(email, password, **extra_fields)


# # class CustomUser(AbstractBaseUser, PermissionsMixin):
# #     """
# #     Custom user model with extended fields.

# #     This model provides a custom implementation of user authentication
# #     and additional fields such as name and phone.
# #     """

# #     email = models.EmailField(unique=True)
# #     name = models.CharField(max_length=100)
# #     phone = models.CharField(max_length=20)
# #     city = models.CharField(max_length=50)
# #     country = models.CharField(max_length=50)
# #     address = models.CharField(max_length=200)
# #     birth_date = models.DateField()

# #     # Other fields specific User model

# #     is_active = models.BooleanField(default=True)
# #     is_staff = models.BooleanField(default=False)

# #     objects = CustomUserManager()

# #     # profile reference
# #     user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE, null=True, blank=True)

# #     USERNAME_FIELD = "email"
# #     REQUIRED_FIELDS = ["name"]

# #     def __str__(self):
# #         return self.email
    


# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# # class UserProfile(models.Model):
# #     """represents a user profile for DonorQuest
# #        keeps track of user's donation target, history, milestones, and badges

# #     """
# #     # user reference
# #     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
# #     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# #     profile_name = models.CharField(max_length=50)
# #     blood_type = models.CharField(max_length=5)
# #     profile_avatar = models.ImageField(upload_to="profile_avatars", blank=True)

# #     # TODO add attributes for tracking milestone, Donation History, Badges etc.
    
# #     # Donation history (assuming a OneToMany relationship with Donation model)
# #     donation_history = models.ManyToManyField(Donation, blank=True)
    
# #     # Milestones, targets, and lives saved
# #     number_of_donations = models.PositiveIntegerField(default=0)
# #     donation_targets = models.ManyToManyField(DonationTarget, blank=True, related_name='user_profiles')
# #     potential_lives_saved = models.PositiveIntegerField(default=0)
  
# #     # getters and setters
# #     def set_blood_type(self, blood_type):
# #         """Sets the user's blood type."""
# #         self.blood_type = blood_type
# #         self.save()
# #     def get_blood_type(self):
# #         """Returns the user's blood type."""
# #         return self.blood_type
    
# #     def set_profile_name(self, profile_name):
# #         """Sets the user's profile name."""
#     #     self.profile_name = profile_name
#     #     self.save()
#     # def get_profile_name(self):
#     #     """Returns the user's profile name."""
#     #     return self.profile_name

#     # def set_donation_target(self, target_amount, target_description=None):
#     #     """Creates or updates a donation target for this user profile."""
#     #     target, created = DonationTarget.objects.get_or_create(user_profile=self, defaults={'target_amount': target_amount, 'target_description': target_description})
        
#     #     if not created:
#     #         target.target_amount = target_amount
#     #         target.target_description = target_description
#     #         target.save()

#     #     return target
#     # def set_profile_avatar(self, profile_avatar):
#     #     """Sets the user's profile avatar."""
#         self.profile_avatar = profile_avatar
#         self.save()
        
#     def get_profile_avatar(self):
#         """Returns the user's profile avatar."""
#         return self.profile_avatar
    
#     def get_donation_targets(self):
#         """Returns a queryset of donation targets associated with this user profile."""
#         return self.donation_targets.all()
    
#     def __str__(self):
#         return self.profile_name

#     def to_dict(self):
#         """returns a dictionary representation of the model"""
#         return {
#             "user_id": self.id,
#             "profile_name": self.profile_name,
#             "blood_type": self.blood_type,
#             "profile_avatar": self.profile_avatar,
#         }

#     def to_json(self):
#         """returns a json representation of the model"""
#         return json.dumps(self.to_dict())

#     class Meta:
#         verbose_name_plural = "User Profiles"

# # class Patient(BaseModel):
# #     """represents a patient"""
#     patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     # ForeignKey to Donor model (assume Donor model is defined elsewhere)
#     # donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
#     blood_type = models.CharField(max_length=5)
#     patient_name = models.CharField(max_length=100)
#     hospital_name = models.CharField(max_length=100)

    # Hide the patient_id and donor_id fields from admin panel
    # Don't show these fields in forms

    # def __str__(self):
    #     """returns a string representation of the model"""
    #     return """Patient Name: {} | Hospital Name: {} | Blood Type: {}""".format(
    #         self.patient_name, self.hospital_name, self.blood_type
    #     )

    # def to_dict(self):
    #     """returns a dictionary representation of the model"""
    #     return {
    #         "patient_id": self.patient_id,
    #         "patient_name": self.patient_name,
    #         "hospital_name": self.hospital_name,
    #         "blood_type": self.blood_type,
    #     }

    # def to_json(self):
    #     """returns a json representation of the model"""
    #     return json.dumps(self.to_dict())

    # class Meta:
    #     """represents a patient"""

    #     verbose_name_plural = "Patients"
# class Donor(models.Model):

#     """represents a donor"""
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     is_registered = models.BooleanField(default=False)
#     DONOR_STATUS = [
#         ('scheduled', 'Scheduled'),
#         ('donated', 'Donated'),
#         ('rejected', 'Rejected'),
#         ('missed_appointment', 'Missed Appointment'),
#     ]
#     donated_for = models.ManyToManyField(Patient, blank=True)
#     donor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     status = models.CharField(max_length=20, choices=DONOR_STATUS, default="scheduled")
   

#     def __str__(self):
#         return str(self.user_profile.user)

#     def to_dict(self):
#         """returns a dictionary representation of the model"""
#         return {
#             "user_id": self.donor_id,
#             "phone_number": self.phone_number,
#             "blood_type": self.blood_type,
#             "birth_date": self.birth_date,
#             "address": self.address,
#             "status": self.status,
#             "city": self.city,
#             "country": self.country,
#         }

#     def to_json(self):
#         """
#         returns a json representation of the model
#         """
#         return json.dumps(self.to_dict())

#     class Meta:
#         verbose_name_plural = "Donors"



# class Donation(BaseModel):
#     """Represents a blood donation"""

#     _DONATION_TYPES = [
#         ('regular', 'Regular'),
#         ('platelets', 'Platelets'),
#         ('plasma', 'Plasma'),
#         ('double_red_cells', 'Double Red Cells'),
#     ]
#     _DONATION_OPTIONS= [
#         ('replacement', 'Replacement'),
#         ('voluntary', 'Voluntary'),
#     ]
#     _STATUS_CHOICES = [
#         ("pending", "Pending"),
#         ("completed", "Completed"),
#         ("canceled", "Canceled"),
#     ]
#     _CONVERSION_RATE = 3

#     donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
#     donation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     # ForeignKey to Donor mode
#     donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
#     blood_type = models.CharField(max_length=5)
#     donation_date = models.DateTimeField(auto_now_add=True)
#     number_of_bags = models.IntegerField()
#     donation_option = models.CharField(
#         max_length=20, choices=_DONATION_OPTIONS, default="Voluntary"
#     )
#     donation_type = models.CharField(
#         max_length=20, choices=_DONATION_TYPES, default="Regular"
#     )
#     status = models.CharField(max_length=20, choices=_STATUS_CHOICES, default="Pending")
#     # capture the number of lives saved by this donation
#     potential_lives_saved = models.PositiveIntegerField(default=0)

#     #  Calculate the number of lives saved by this donation
#     def calculate_lives_saved(self):
#         """Calculate potential lives saved based on the donation amount and conversion rate."""
#         self.potential_lives_saved = int(self.number_of_bags  * self._CONVERSION_RATE)
#         self.save()
        
#     def __str__(self):
#         return f"Donation by {self.donor.user_profile.user}"

#     def to_dict(self):
#         """returns a dictionary representation of the model"""
#         return {
#             "donation_id": self.donation_id,
#             "donor_id": self.donor_id,
#             "blood_type": self.blood_type,
#             "donation_date": self.donation_date,
#             "status": self.status,
#         }

#     def to_json(self):
#         """returns a json representation of the model"""
#         return json.dumps(self.to_dict())

#     class Meta:
#         verbose_name_plural = "Blood Donations"


# class DonationTarget(models.Model):
#     """Represents a donation target set by a user."""

#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     target_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     target_description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Target for {self.user_profile.profile_name}"

#     class Meta:
#         verbose_name_plural = "Donation Targets"




# class DonationRequest(Patient):
#     """represents a request for blood donation"""
#     __BUFFER_SCALE = 2
#     __INTERESTED_DONOR_IDs = {}
#     request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
#     # ForeignKey to Organizer model (assume Organizer model is defined elsewhere)
#     # organizer_id = models.ForeignKey(Organizer, on_delete=models.CASCADE)

#     number_of_pints = models.PositiveIntegerField()
#     request_date = models.DateTimeField(auto_now_add=True)
#     patient_story = models.TextField()
#     patient_avatar = models.ImageField(upload_to="patient_avatars", blank=True)
    

#     STATUS_CHOICES = [
#         ("Listed", "Listed"),
#         ("Pending", "Pending"),
#         ("Stale", "Stale"),
#         ("Completed", "Completed"),
#         ("canceled", "Canceled"),
#     ]
#     TAGS = [
#         ('Critical Emergency', 'Critical Emergency'),
#         ('Urgent', 'Urgent'),
#         ('Normal', 'Normal'),
#     ]
#     tags = models.CharField(max_length=20, choices=TAGS, default="Normal")
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

#     donors_needed = models.PositiveIntegerField(default=1)
    
#     ### TODO consider fixing these section 
#     # or move them to the business logic ####

#     # calculate number of donors needed based on pints
#     def update_donors_needed(self):
#         """returns the number of donors needed"""	
#         return self.number_of_pints * self.BUFFER_SCALE
   
#     # decrement the number of donors needed by 1 if 
#     # user gets added to interested_donor_ids

#     def decrement_donors_needed(self):
#         """decrements the number of donors needed by 1 for each interested donors,
#           depending on the staus of each donor's donation status"""
#         if self.donors_needed > 0:
#             pass
#     # update donors needed
#     # if self.number_of_pints:
#     #     self.donors_needed = self.update_donors_needed()
    
#     ### TODO consider fixing these section
#     #  or move them to the business logic ####

#     # Hide the request_id and organizer_id fields from admin panel
#     # Don't show these fields in forms
#     def __str__(self):
#         return self.patient_name

#     def to_dict(self):
#         """returns a dictionary representation of the model"""
#         return {
#             "request_id": self.request_id,
#             "patient_name": self.patient_name,
#             "hospital_name": self.hospital_name,
#             "blood_type": self.blood_type,
#             "donors_needed": self.donors_needed,
#             "request_date": self.request_date,
#             "patient_story": self.patient_story,
#             "status": self.status,
#             "interested_donor_ids": self.interested_donor_ids,
#         }

#     def to_json(self):
#         """returns a json representation of the model"""
#         return json.dumps(self.to_dict())

#     class Meta:
#         verbose_name_plural = "Donation Requests"

# class Organizer(BaseModel):
#     """represents organizer of blood donation events"""
#     # TODO add appropriate attributes and methods

#     class Meta:
#         verbose_name_plural = "Organizers"