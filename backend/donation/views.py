from django.shortcuts import render, redirect
from .forms import DonationRequestForm
from .models import DonationRequest

def create_request(request):

    """ creates a new donation request
    """
    if request.method == 'POST':
        form = DonationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_donation_request = form.save()
            return redirect('/list_requests/')
    else:
        form = DonationRequestForm()
    
    return render(request, 'create_request.html', {'form': form})
  
def request_list(request):
    """ returns a list of donation requests
    """
    donation_requests = DonationRequest.objects.all()
    return render(request, './list_requests.html', {'donation_requests': donation_requests})

