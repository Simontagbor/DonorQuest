from django.db import models # noqa: E402
# from .donation import Donation
from .donationtarget import DonationTarget # noqa: F401
import json
from django.contrib.auth.models import User # noqa: E402
from .base import BaseModel # noqa: E402

class UserProfile(BaseModel): 
    """represents a user profile for DonorQuest
       keeps track of user's donation target, history, milestones, and badges
    """
    # user reference
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_name = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=5)
    profile_avatar = models.ImageField(upload_to="profile_avatars", blank=True)
    city = models.CharField(max_length=50, blank=True)
    
    # Donation history (assuming a OneToMany relationship with Donation model)
    donation_history = models.ForeignKey("Donation", on_delete=models.CASCADE,
                                         blank=True, null=True)
    
    # Milestones, targets, and lives saved
    target_donations = models.PositiveIntegerField(default=0)
    number_of_donations = models.PositiveIntegerField(default=0)
    donation_targets = models.ForeignKey(DonationTarget,
                                         on_delete=models.CASCADE,
                                         blank=True, related_name='user_profiles',
                                         null=True
                                        ) 
    
    potential_lives_saved = models.PositiveIntegerField(default=0)
  
    # getters and setters
    def set_blood_type(self, blood_type):
        """Sets the user's blood type."""
        self.blood_type = blood_type
        self.save()
    def get_blood_type(self):
        """Returns the user's blood type."""
        return self.blood_type
    
    def set_profile_name(self, profile_name):
        """Sets the user's profile name."""
        self.profile_name = profile_name
        self.save()
    def get_profile_name(self):
        """Returns the user's profile name."""
        return self.profile_name

    def set_donation_target(self, target_amount, target_description=None):
        """Creates or updates a donation target for this user profile."""
        target, created = DonationTarget.objects.get_or_create(
            user_profile=self, 
            defaults={'target_amount': target_amount, 
                      'target_description': target_description}
        )
        if not created:
            target.target_amount = target_amount
            target.target_description = target_description
            target.save()

        return target
    def set_profile_avatar(self, profile_avatar):
        """Sets the user's profile avatar."""
        self.profile_avatar = profile_avatar
        self.save()
        
    def get_profile_avatar(self):
        """Returns the user's profile avatar."""
        return self.profile_avatar
    
    def get_donation_targets(self):
        """Returns a queryset of donation targets associated with this user profile."""
        return self.donation_targets.all()
    
    def __str__(self):
        return self.profile_name

    def to_dict(self):
        """returns a dictionary representation of the model"""
        return {
            "user_id": self.id,
            "profile_name": self.profile_name,
            "blood_type": self.blood_type,
            "profile_avatar": self.profile_avatar,
        }

    def to_json(self):
        """returns a json representation of the model"""
        return json.dumps(self.to_dict())

    class Meta:
        """represents a user profile"""
        verbose_name_plural = "User Profiles"
