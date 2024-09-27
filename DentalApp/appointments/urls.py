from django.urls import path
from .views import ServiceListView, AppointmentCreateView, PatientAppointmentListView, auth0_callback

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-list'),
    path('patients/<int:patient_id>/appointments/', PatientAppointmentListView.as_view(), name='patient-appointments'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='create-appointment'),
    path('auth/callback/', auth0_callback, name='auth0-callback'),
]
