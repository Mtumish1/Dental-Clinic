from django.urls import path
from .views import ServiceListView, AppointmentCreateView, PatientAppointmentListView

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/<int:patient_id>/', PatientAppointmentListView.as_view(), name='patient-appointments'),
]
