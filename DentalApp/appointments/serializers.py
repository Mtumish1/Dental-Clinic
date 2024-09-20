from rest_framework import serializers
from .models import Service, Patient, Appointment

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    service = ServiceSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        service_data = validated_data.pop('service')

        patient, _ = Patient.objects.get_or_create(**patient_data)
        service = Service.objects.get(id=service_data['id'])

        appointment = Appointment.objects.create(patient=patient, service=service, **validated_data)
        return appointment
