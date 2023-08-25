from django import forms
from .models import DonationRequest

class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['patient_name', 
                  'blood_type', 
                  'hospital_name', 
                  'patient_story', 
                  'patient_avatar', 
                  'tags', 
                  'number_of_pints'
                  ]