from django.test import TestCase
from donation.models import DonationRequest
from .views import create_request

# Create your tests here.
class TestDonationRequest(TestCase):
    def setUp(self):
        self.donation_request = DonationRequest(
            patient_name="John Doe",
            blood_type="O+",
            hospital="Kenyatta National Hospital",
            patient_story="John Doe is a patient at KNH",
            patient_avatar="/static/images/avatar.png",
            tags="Urgent",
            number_of_pints=2
        )
        self.donation_request.save()

    def test_create_request(self):
        self.assertEqual(self.donation_request.patient_name, "John Doe")
        self.assertEqual(self.donation_request.blood_type, "O+")
        self.assertEqual(self.donation_request.hospital_name, "Kenyatta National Hospital") # noqa: E501
        self.assertEqual(self.donation_request.patient_story, "John Doe is a patient at KNH") # noqa: E501
        self.assertEqual(self.donation_request.patient_avatar, "/static/images/avatar.png") # noqa: E501
        self.assertEqual(self.donation_request.tags, "Urgent")
        self.assertEqual(self.donation_request.number_of_pints, 2)
    
    def test_create_request_view(self):
        self.assertEqual(create_request(self.request), "request_list")
        
class TestCreateDonation(TestCase):
    def setUp(self):
        self.donation_request = DonationRequest(
            patient_name="John Doe",
            blood_type="O+",
            hospital="Kenyatta National Hospital",
            patient_story="John Doe is a patient at KNH",
            patient_avatar="/static/images/avatar.png",
            tags="Urgent",
            number_of_pints=2
        )
        self.donation_request.save()

    def test_create_request(self):
        self.assertEqual(self.donation_request.patient_name, "John Doe")
        self.assertEqual(self.donation_request.blood_type, "O+")
        self.assertEqual(self.donation_request.hospital, "Kenyatta National Hospital")
        self.assertEqual(self.donation_request.patient_story, "John Doe is a patient at KNH") # noqa: E501
        self.assertEqual(self.donation_request.patient_avatar, "/static/images/avatar.png") # noqa: E501
        self.assertEqual(self.donation_request.tags, "Urgent")
        self.assertEqual(self.donation_request.number_of_pints, 2)
    
    def test_create_request_view(self):
        self.assertEqual(create_request(self.donation_request), "John Doe")
        self.assertEqual(create_request(self.donation_request), "O+")
        self.assertEqual(create_request(self.donation_request), "Kenyatta National Hospital") # noqa: E501
        self.assertEqual(create_request(self.donation_request), "John Doe is a patient at KNH") # noqa: E501
        self.assertEqual(create_request(self.donation_request), "/static/images/avatar.png") # noqa: E501
        self.assertEqual(create_request(self.donation_request), "Urgent")
        self.assertEqual(create_request(self.donation_request), 2)
    def tearDown(self):
        self.donation_request.delete()

class TestDonationRequestModel(TestCase):
    def setUp(self):
        self.donation_request = DonationRequest(
            patient_name="John Doe",
            blood_type="O+",
            hospital="Kenyatta National Hospital",
            patient_story="John Doe is a patient at KNH",
            patient_avatar="/static/images/avatar.png",
            tags="Urgent",
            number_of_pints=2
        )
        self.donation_request.save()

    def test_donation_request_model(self):
        self.assertEqual(self.donation_request.patient_name, "John Doe")
        self.assertEqual(self.donation_request.blood_type, "O+")
        self.assertEqual(self.donation_request.hospital, "Kenyatta National Hospital")
        self.assertEqual(self.donation_request.patient_story, "John Doe is a patient at KNH") # noqa: E501
        self.assertEqual(self.donation_request.patient_avatar, "/static/images/avatar.png") # noqa: E501
        self.assertEqual(self.donation_request.tags, "Urgent")
        self.assertEqual(self.donation_request.number_of_pints, 2)
    
    def tearDown(self):
        self.donation_request.delete()


class TestDonationRequestView(TestCase):
    def setUp(self):
        self.donation_request = DonationRequest(
            patient_name="John Doe",
            blood_type="O+",
            hospital="Kenyatta National Hospital",
            patient_story="John Doe is a patient at KNH",
            patient_avatar="/static/images/avatar.png",
            tags="Urgent",
            number_of_pints=2
        )
        self.donation_request.save()

    def test_donation_request_view(self):
        self.assertEqual(create_request(self.donation_request), "John Doe")
        self.assertEqual(create_request(self.donation_request), "O+")
        self.assertEqual(create_request(self.donation_request), "Kenyatta National Hospital") # noqa: E501
        self.assertEqual(create_request(self.donation_request), "John Doe is a patient at KNH") # noqa: E501
        self.assertEqual(create_request(self.donation_request), "/static/images/avatar.png") # noqa: E501
        self.assertEqual(create_request(self.donation_request), "Urgent")
        self.assertEqual(create_request(self.donation_request), 2)
    
    def tearDown(self):
        self.donation_request.delete()

class TestDonationRequestForm(TestCase):
    def setUp(self):
        self.donation_request = DonationRequest(
            patient_name="John Doe",
            blood_type="O+",
            hospital="Kenyatta National Hospital",
            patient_story="John Doe is a patient at KNH",
            patient_avatar="/static/images/avatar.png",
            tags="Urgent",
            number_of_pints=2
        )
        self.donation_request.save()

    def test_donation_request_form(self):
        self.assertEqual(self.donation_request.patient_name, "John Doe")
        self.assertEqual(self.donation_request.blood_type, "O+")
        self.assertEqual(self.donation_request.hospital, "Kenyatta National Hospital")
        self.assertEqual(self.donation_request.patient_story, "John Doe is a patient at KNH")  # noqa: E501
        self.assertEqual(self.donation_request.patient_avatar, "/static/images/avatar.png")# noqa: E501
        self.assertEqual(self.donation_request.tags, "Urgent")
        self.assertEqual(self.donation_request.number_of_pints, 2)
    
    def tearDown(self):
        self.donation_request.delete()