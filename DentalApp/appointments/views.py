from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Service, Appointment, Patient 
from .serializers import ServiceSerializer, AppointmentSerializer
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings
import requests
from .sms_service import send_appointment_sms



# List all available services
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Create a new appointment
class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        appointment = serializer.save()  # Save the appointment

        # Retrieve patient and appointment details
        patient = appointment.patient
        service = appointment.service
        appointment_date = appointment.appointment_date
        appointment_time = appointment.appointment_time
        checkin_code = appointment.checkin_code

        # Send SMS to the patient
        send_appointment_sms(
            phone_number=patient.phone_number,
            service_name=service.name,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            checkin_code=checkin_code
        )


# View a patient's appointments
class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')

        if not self.request.user.is_staff and self.request.user.id != int(patient_id):
            raise PermissionDenied("You are not allowed to view this patient's appointments.")
            
        return Appointment.objects.filter(patient__id=patient_id)



# Handle the Auth0 response, create/retrieve user, and log them in
def auth0_callback(request):
    code = request.GET.get('code')
    token_url = f'https://{settings.AUTH0_DOMAIN}/oauth/token'
    
    # Exchange the code for a token
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': settings.AUTH0_CLIENT_ID,
        'client_secret': settings.AUTH0_CLIENT_SECRET,
        'redirect_uri': settings.AUTH0_CALLBACK_URL,
        'code': code
    }
    
    token_response = requests.post(token_url, json=token_data)
    tokens = token_response.json()

    # Fetch the user info from Auth0
    user_info_url = f'https://{settings.AUTH0_DOMAIN}/userinfo'
    headers = {'Authorization': f"Bearer {tokens['access_token']}"}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    # Create or get the user from the database based on the Auth0 user_id or email
    user, created = User.objects.get_or_create(username=user_info['email'])
    
    # Log the user in
    login(request, user)

    # Redirect to the appointments page after login
    return redirect('/appointments/')