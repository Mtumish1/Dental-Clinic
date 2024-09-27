import random
import string
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User





class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.DurationField()  # e.g., 1 hour

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ]
    created_at = models.DateTimeField(auto_now_add=True)

    checkin_code = models.CharField(max_length=8, unique=True, blank=True)   #Variable to store the unique alphanumeric code fir Mpesa billing

    def save(self, *args, **kwargs):
        self.validate_appointment_date_time()
        if not self.checkin_code:        # Generate and assign check-in code if not already assigned
            self.checkin_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Generate a random alphanumeric code of length 8


    def validate_appointment_date_time(self):    # Ensure the appointment date and time are not in the past
        appointment_datetime = timezone.make_aware(
            timezone.datetime.combine(self.appointment_date, self.appointment_time)
        )
        if appointment_datetime < timezone.now():
            raise ValidationError("Appointment cannot be scheduled in the past.")

    def __str__(self):
        return f'{self.patient} - {self.service} on {self.appointment_date} at {self.appointment_time}'
    class Meta:
        ordering = ['appointment_date', 'appointment_time']