from django.shortcuts import render, redirect
from .models import DonationRequest

def create_request(request):

    """ creates a new donation request
    """
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        blood_type = request.POST.get('blood_type')
        hospital = request.POST.get('hospital')
        patient_story = request.POST.get('patient_story')
        patient_avatar = request.FILES.get('patient_avatar')
        tags = request.POST.get('tags')
        number_of_pints = request.POST.get('number_of_pints')
        
        # ToDo validation and fault-tolerant logic before creation of request
        #create a new donation request
        new_donation_request = DonationRequest.objects.create(
            patient_name=patient_name,
            blood_type=blood_type,
            hospital_name=hospital,
            patient_story=patient_story,
            patient_avatar=patient_avatar,
            tags=tags,
            number_of_pints=number_of_pints
        )
        new_donation_request.save()
        return redirect('http://127.0.0.1:8000/list_requests/')
    return render(request, './create_request.html', {})

# Create your views here.
def request_list(request):
    """ returns a list of donation requests
    """
    donation_requests = DonationRequest.objects.all()
    return render(request, './list_requests.html', {'donation_requests': donation_requests})

