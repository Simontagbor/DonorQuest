from django.db import models
from .base import BaseModel
from .drive import DonationDrive
from .socialmediaprofile import SocialMediaProfile
from .testimonial import Testimonial

class DonationDriveOrganizer(BaseModel):
    """
    Represents an organizer of a donation drive.
    Drive organizers are users who want to organize donation drives.
    they can create donation drives.
    """

    organizer_name = models.CharField(max_length=100)
    profile_avatar = models.ImageField(upload_to="organizer_avatars", blank=True)
    biography = models.TextField(blank=True)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    availability = models.BooleanField(default=True)
    organizer_rating = models.DecimalField(max_digits=3, decimal_places=2)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    # Define a relationship to upcoming DonationDrives
    upcoming_donation_drives = models.ManyToManyField(DonationDrive, blank=True)
    # Social media profiles (using a related model)
    social_media_profiles = models.ManyToManyField(SocialMediaProfile,
                                                   blank=True, related_name='organizers')

    # References or Testimonials (using a related model)
    testimonials = models.ManyToManyField(Testimonial, blank=True, 
                                          related_name='organizers')


    # getters and setters

    def get_donation_drives(self):
        """
        Get the list of donation drives for the organizer.

        Returns:
            QuerySet: A queryset of DonationDrive 
            objects associated with the organizer.
        """
        return self.donation_drives.all()
    
    def get_testimonials(self):
        """
        Get the list of testimonials for the organizer.

        Returns:
            QuerySet: A queryset of Testimonial 
            objects associated with the organizer.
        """
        return self.testimonials.all()

    def set_social_media_profile(self, platform, link):
        """
        Add a social media profile to the organizer's list of profiles.
        
        Args:
            platform (str): The name of the social media platform (e.g., "Facebook").
            link (str): The URL link to the organizer's profile on the platform.
        """
        social_media_profile, created = self.social_media_profiles.get_or_create(
            platform=platform, defaults={'link': link})
        if not created:
            social_media_profile.link = link
            social_media_profile.save()

    def get_social_media_profiles(self):
        """
        Get the list of social media profiles for the organizer.

        Returns:
            QuerySet: A queryset of SocialMediaProfile 
            objects associated with the organizer.
        """
        return self.social_media_profiles.all()
    
    def __str__(self):
        return f"DonationDrive Organizer: {self.organizer_name}"
    