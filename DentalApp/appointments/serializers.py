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

class AppointmentSerializer(serializers.ModelSerializer):       #Using service and patient IDs as the request payload
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)
        return appointment
