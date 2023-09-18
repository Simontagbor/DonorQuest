from django.db import models
from .base import BaseModel
from .drive import DonationDrive
from .userprofile import UserProfile
from donation.models.donation import Donation
from .hospital import Hospital

class DonationPlan(BaseModel):
    """Represents a donation plan set by a user.
    Attributes: target_donations, user_profile, 
                pending_donations, selected_drives, 
                preferred_hospital
    Functions: generate_donation_plan is used to generate a donation plan
    usage: donation_plan = DonationPlan.objects.create()
    """	
    target_donations = models.PositiveIntegerField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pending_donations = models.ManyToManyField(Donation)
    selected_drives = models.ManyToManyField(DonationDrive, through='DonationPlanDrive')
    preferred_hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, 
                                           null=True, blank=True)   

    @classmethod
    def generate_donation_plan(cls, user_profile):
        """Generates a donation plan for the user_profile.
        The donation plan will contain donations for donation drives in the user's city.
        The number of donations will be equal to 
        the target_donations attribute of the user_profile.
        Usage: donation_plan = DonationPlan.generate_donation_plan(user_profile)
        Returns: donation_plan
        """
        # Calculate the number of donations needed to reach the target
        target_donations = user_profile.target_donations
        city = user_profile.city

        # Query for donation drives in the user's city
        donation_drives = DonationDrive.objects.filter(location__iexact=city)

        if not donation_drives:
            # query for the nearest hospital based on the user's location
            # TODO 'find_nearest_hospital' to find the nearest hospital
            nearest_hospital = Hospital.objects.filter(location__iexact=city) #simple filter for now

            if nearest_hospital:
                donation_drives = [DonationDrive(location=nearest_hospital.location)]

        # Create donations for each drive and add them to the plan
        donation_plan = cls.objects.create(target_donations=target_donations,
                                           user_profile=user_profile)
        donations_created = 0

        for drive in donation_drives:
            if donations_created >= target_donations:
                break  # Stop if the target is reached

            # Create a pending donation for the drive
            donation = Donation.objects.create(
                donation_drive=drive,
                donation_plan=donation_plan,
                status="Pending",
                donation_location=drive.location,
                scheduled_date=drive.scheduled_date,
                scheduled_time=drive.scheduled_time, 
                donor=user_profile.user
            )

            donation_plan.donations.add(donation)
            donations_created += 1

        return donation_plan

    def __str__(self):
        """Returns a string representation of the donation plan."""
        return f"Donation plan for {self.user_profile.profile_name}"


class DonationPlanDrive(models.Model):
    donation_plan = models.ForeignKey(DonationPlan, on_delete=models.CASCADE)
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    # Other fields as needed