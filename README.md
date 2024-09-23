Dental Appointment Scheduling Django Microservice

This project is a Patient Appointment Scheduling Microservice built using Django and Django REST Framework. It features authentication using Auth0 and Africa's Talking SMS integration to notify patients upon appointment creation.

Features
Appointment Scheduling: Patients can schedule appointments for various dental services.
Authentication: Secured user authentication via Auth0 using OpenID Connect.
SMS Notifications: When an appointment is created, the system sends an SMS notification to the patient using Africa's Talking.
REST API: Provides RESTful endpoints for interacting with appointments and services.
CI/CD Setup: Ready for continuous integration and deployment, with unit tests for core functionality.

Tech Stack
Backend: Django, Django REST Framework
Authentication: Auth0 (OpenID Connect)
SMS Service: Africa's Talking
Database: SQLite (can be swapped for PostgreSQL, MySQL, etc.)
Other: Docker (optional, for deployment), CI/CD tools (GitHub Actions, etc.)
Prerequisites
Python 3.8+
Django 5.1+
Africa's Talking API Key (Sign up for Africa's Talking)
Auth0 Account (Sign up for Auth0)
Installation
Clone the repository:

git clone https://github.com/Mtumish1/DENTAL-CLINIC.git
cd dental-appointment-service

Set up a virtual environment:
python3 -m venv env
source env/bin/activate
Install the dependencies:

pip install -r requirements.txt

Create a .env file in the root directory and add the following environment variables:

SECRET_KEY=your_django_secret_key
AUTH0_CLIENT_ID=your_auth0_client_id
AUTH0_CLIENT_SECRET=your_auth0_client_secret
AUTH0_DOMAIN=your_auth0_domain
AFRICAS_TALKING_API_KEY=your_africas_talking_api_key
AFRICAS_TALKING_USERNAME=your_africas_talking_username

Run database migrations:
python manage.py migrate

Create a superuser to access the admin panel:
python manage.py createsuperuser

Run the development server:
python manage.py runserver
Authentication Setup (Auth0)
Create an Auth0 Account and set up a new application.

In the Auth0 Dashboard, set the following:
Allowed Callback URLs: http://127.0.0.1:8000/accounts/auth0/callback/
Allowed Logout URLs: http://127.0.0.1:8000
Allowed Web Origins: http://127.0.0.1:8000

Configure Socialaccount Providers in settings.py:
SOCIALACCOUNT_PROVIDERS = {
'openid_connect': {
'APP': {
'client_id': os.getenv('AUTH0_CLIENT_ID'),
'secret': os.getenv('AUTH0_CLIENT_SECRET'),
'issuer': f'https://{os.getenv('AUTH0_DOMAIN')}',
}
}
}
SMS Notifications (Africa's Talking)
Sign up for an Africa's Talking account and get your API key and username.

Ensure the following environment variables are set in your .env file:
AFRICAS_TALKING_API_KEY=your_africas_talking_api_key
AFRICAS_TALKING_USERNAME=your_africas_talking_username
The SMS notifications are triggered in the send_appointment_sms function located in sms_service.py.

API Endpoints
List Services: GET /api/services/
Create Appointment: POST /api/appointments/create/
View Patient Appointments: GET /api/patients/<patient_id>/appointments/
Auth0 Login Callback: GET /auth/callback/

Running Unit Tests
To run unit tests:
python manage.py test

Tests are defined for:
Appointment creation
SMS sending functionality using Africa's Talking
Auth0 authentication flow
Deployment
To deploy the application, follow these steps:

Ensure that your environment variables are set correctly in your production environment.
Use Docker for containerized deployment (optional).
Set up CI/CD pipelines for continuous integration and deployment (using GitHub Actions or other tools).

License
This project is licensed under the MIT License.
