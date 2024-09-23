import africastalking
from django.conf import settings

# Initialize Africa's Talking API
africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_appointment_sms(phone_number, service_name, appointment_date, appointment_time, checkin_code):
    message = (
        f"Your appointment for {service_name} is confirmed on {appointment_date} at {appointment_time}. "
        f"Your check-in code is: {checkin_code}. Please present this code during your visit."
    )
    try:
        response = sms.send(message, [phone_number])
        print(response)
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None

