from django.db import models

class SocialMediaProfile(models.Model):
    platform = models.CharField(max_length=100)
    link = models.URLField()