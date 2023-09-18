from django.db import models

class DonationDrive(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey('DonationDriveOrganizer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
