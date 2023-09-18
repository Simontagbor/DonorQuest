from django.db import models
from django.utils import timezone
from .userprofile import UserProfile  

class Hospital(models.Model):
    """ represents a hospital
    Attributes: name, city, country, address, contact_number, email
    functions: __str__ for string representation
    usage: hospital = Hospital.objects.create(
                                                name="Hospital Name", 
                                                city="City Name", 
                                                country="Country Name", 
                                                address="Address", 
                                                contact_number="Contact Number", 
                                                email="Email")
    """
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name



class HospitalAppointment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Canceled", "Canceled"),
    ], default="Scheduled")

    def __str__(self):
        return f"{self.user_profile}'s Appointment at {self.hospital}"