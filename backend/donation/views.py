from django.shortcuts import render, redirect, get_object_or_404
from .models.donationrequest import DonationRequest
from django.views.generic import TemplateView
from .forms import RandomDonationForm, DonationRequestForm, SpecificDonationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'index.html')

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('home')  # Replace 'home' with the appropriate URL name.
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/list_requests/')  # Redirect to your home page after login
    else:
        form = AuthenticationForm()
    
    return render(request, './registration/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to your home page after logout

# Create donation request view
def create_request(request):
    """ creates a new donation request """
    if request.method == 'POST':
        form = DonationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_donation_request = form.save()
            return redirect('/list_requests/')
    else:
        form = DonationRequestForm()
    
    return render(request, 'create_request.html', {'form': form})

# List donation requests view
def request_list(request):
    """ returns a list of donation requests """
    donation_requests = DonationRequest.objects.all()
    return render(request, 'list_requests.html', {'donation_requests': donation_requests})

# Handle creation of random Donations view
def random_donation_view(request):
    """ creates a new random donation """
    if request.method == 'POST':
        form = RandomDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user.donor
            donation.save()
            donation.calculate_lives_saved()
            return redirect('/thank-you/')
    else:
        form = RandomDonationForm()
    return render(request, 'random_donation.html', {'form': form})

# Handle creation of specific Donations view
def specific_patient_donation_view(request, request_id):
    """Creates a new donation for a specific patient."""
    donation_request = get_object_or_404(DonationRequest, id=request_id)
    
    if request.method == 'POST':
        form = SpecificDonationForm(request.POST, initial={'donation_request': donation_request})
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user.donor
            donation.donation_request = donation_request
            donation.save()
            donation.calculate_lives_saved()
            return redirect('/success_page/')  # Redirect to success page
    else:
        form = SpecificDonationForm(initial={'donation_request': donation_request})
    
    return render(request, 'specific_patient_donation.html', {'form': form, 'donation_request': donation_request})

# Thank You view
class ThankYouView(TemplateView):
    template_name = 'thank_you.html'
