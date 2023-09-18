from django import forms
from donation.models.donation import Donation
from donation.models.donationrequest import DonationRequest
from donation.models.userprofile import UserProfile

class DonationRequestForm(forms.ModelForm):
    """Form for creating a new donation request."""
    class Meta:
        model = DonationRequest
        exclude = ['request_date']  # Exclude the non-editable field
        fields = [
            'patient_name',
            'patient_story',
            'blood_group',
            'patient_avatar',
            'number_of_pints',
            'hospital',
        ]

class BaseDonationForm(forms.ModelForm):
    """Base form for creating a new donation."""
    class Meta:
        model = Donation
        fields = [
            'donor_name',
            'donor_phone',
            'donation_request',
            'blood_group',
            'number_of_pints',
            'scheduled_date',
            'scheduled_time',
            'donation_option',
            'donation_type',
        ]
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'scheduled_time': forms.TimeInput(attrs={'class': 'timepicker'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        donation_request = cleaned_data.get('donation_request')

        
class RandomDonationForm(BaseDonationForm):
    """Form for creating a new random donation."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['donation_request'].required = False
        self.fields['scheduled_date'].required = False

class SpecificDonationForm(BaseDonationForm):
    """Form for creating a new donation request."""
    def __init__(self, *args, **kwargs):
        donation_request_obj = kwargs.pop('donation_request', None)
        super().__init__(*args, **kwargs)
        self.fields['donation_request'].widget = forms.HiddenInput()

        if donation_request_obj:
            self.fields['donation_request'].initial = donation_request_obj.donation_request
            
        # if not donation_request_obj:
        #     raise forms.ValidationError("Donation request must be selected.")


class UserProfileForm(forms.ModelForm):
    """Form for creating a new user profile."""
    class Meta:
        model = UserProfile
        fields = ['profile_name', 'blood_type', 'profile_avatar']
