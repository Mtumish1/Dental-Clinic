from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.DurationField()  # e.g., 1 hour

    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    #Variable to store the unique alphanumeric code
    checkin_code = models.CharField(max_length=8, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.checkin_code:        # Generate and assign check-in code if not already assigned
            self.checkin_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Generate a random alphanumeric code of length 8


    def __str__(self):
        return f'{self.patient} - {self.service} on {self.appointment_date} at {self.appointment_time}'
