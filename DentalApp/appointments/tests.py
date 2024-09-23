from django.test import TestCase
from unittest.mock import patch
from .models import Appointment, Patient, Service
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Mock the send_sms function
from .sms_service import send_appointment_sms

class SMSIntegrationTest(TestCase):
    
    def setUp(self):
        # Set up test data
        self.patient = Patient.objects.create(
            first_name='John', last_name='Doe', phone_number='+254711111111'
        )
        self.service = Service.objects.create(
            name='Teeth Cleaning', description='Professional dental cleaning'
        )
        self.client = APIClient()

    @patch('appointments.sms_service.send_appointment_sms') # Mock send_sms to avoid sending actual SMS
    def test_sms_sent_on_appointment_creation(self, mock_send_sms):
        """Test that SMS is sent when a new appointment is created."""
        
        # Define the appointment data
        appointment_data = {
            'service': self.service.id,
            'patient': self.patient.id,
            'date_time': '2024-09-30T14:30:00Z'
        }
        
        # Send a POST request to create an appointment
        response = self.client.post(reverse('create-appointment'), appointment_data, format='json')
        
        # Assert the appointment was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that send_sms was called
        mock_send_sms.assert_called

