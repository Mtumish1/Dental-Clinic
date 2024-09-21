from rest_framework import generics
from .models import Service, Appointment, Patient 
from .serializers import ServiceSerializer, AppointmentSerializer

# List all available services
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Create a new appointment
class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# View a patient's appointments
class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Appointment.objects.filter(patient__id=patient_id)
