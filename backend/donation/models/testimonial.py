from django.db import models
from django.contrib.auth.models import User

class Testimonial(models.Model):
    reference_text = models.TextField()
    reference_by = models.ForeignKey(User, on_delete=models.CASCADE)