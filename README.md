# Dental Appointment Scheduling Django Microservice

This project is a Patient Appointment Scheduling Microservice built with Django and Django REST Framework. It includes authentication and authorization via Auth0 and integrates with Africa's Talking SMS API to notify patients of their appointments.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Authentication Setup (Auth0)](#authentication-setup-auth0)
- [SMS Notifications (Africa's Talking)](#sms-notifications-africas-talking)
- [API Endpoints](#api-endpoints)
- [Running Unit Tests](#running-unit-tests)
- [Deployment](#deployment)
- [License](#license)

## Features

- **Appointment Scheduling**: Patients can schedule appointments for various dental services.
- **Authentication & Authorization**: Secured user authentication via Auth0 using OpenID Connect.
- **SMS Notifications**: Automatic SMS notifications sent to patients upon appointment creation using Africa's Talking.
- **REST API**: Provides RESTful endpoints for interacting with appointments and services.
- **CI/CD Setup**: Ready for continuous integration and deployment, with unit tests for core functionality.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: Auth0 (OpenID Connect)
- **SMS Service**: Africa's Talking
- **Database**: SQLite (can be swapped for PostgreSQL, MySQL, etc.)
- **Other**: Docker (optional for deployment), CI/CD tools (GitHub Actions, etc.)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: 3.8+
- **Django**: 5.1+
- **Africa's Talking API Key**: [Sign up for Africa's Talking](https://africastalking.com/)
- **Auth0 Account**: [Sign up for Auth0](https://auth0.com/)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Mtumish1/Dental-Clinic.git
   cd dental-appointment-service

   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate

   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt

   ```

4. **Create a .env file in the root directory and add the following environment variables**:

   ```bash
   SECRET_KEY=your_django_secret_key
   AUTH0_CLIENT_ID=your_auth0_client_id
   AUTH0_CLIENT_SECRET=your_auth0_client_secret
   AUTH0_DOMAIN=your_auth0_domain
   AFRICAS_TALKING_API_KEY=your_africas_talking_api_key
   AFRICAS_TALKING_USERNAME=your_africas_talking_username

   ```

5. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser to access the admin panel**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Authentication Setup (Auth0)

1. Create an Auth0 Account and set up a new application.
2. In the Auth0 Dashboard, configure the following:

- Allowed Callback URLs: http://127.0.0.1:8000/accounts/auth0/callback/
- Allowed Logout URLs: http://127.0.0.1:8000
- llowed Web Origins: http://127.0.0.1:8000

3. Configure Social Account Providers in settings.py:

```python
SOCIALACCOUNT_PROVIDERS = {
    'openid_connect': {
        'APP': {
            'client_id': os.getenv('AUTH0_CLIENT_ID'),
            'secret': os.getenv('AUTH0_CLIENT_SECRET'),
            'issuer': f'https://{os.getenv('AUTH0_DOMAIN')}',
        }
    }
}
```

## SMS Notifications (Africa's Talking)

1. Sign up for an Africa's Talking account and get your API key and username.
2. Ensure the following environment variables are set in your .env file:

````bash
AFRICAS_TALKING_API_KEY=your_africas_talking_api_key
AFRICAS_TALKING_USERNAME=your_africas_talking_username ```

The SMS notifications are triggered in the ``send_appointment_sms`` function located in ``sms_service.py``.
````

## API Endpoints

- **List Services**:

  - **Method**: `GET`
  - **Endpoint**: `/api/services/`
  - **Authorization**: Not required

- **Create Appointment**:

  - **Method**: `POST`
  - **Endpoint**: `/api/appointments/create/`
  - **Authorization**: Required
  - **Request Body**:
    ```json
    {
      "patient": {
        "name": "John Doe",
        "phone_number": "+254700000000"
      },
      "service": {
        "id": 1
      },
      "appointment_date": "2024-10-01",
      "appointment_time": "14:00"
    }
    ```

- **View Patient Appointments**:

  - **Method**: `GET`
  - **Endpoint**: `/api/patients/<patient_id>/appointments/`
  - **Authorization**: Required

- **Auth0 Login Callback**:
  - **Method**: `GET`
  - **Endpoint**: `/auth/callback/`
  - **Authorization**: Not required

## Running Unit Tests

To run unit tests:

```bash
python manage.py test
```

Tests are defined for:

- Appointment creation
- SMS sending functionality using Africa's Talking
- Auth0 authentication flow

## Deployment

To deploy the application, follow these steps:

1. Ensure that your environment variables are set correctly in your production environment.
2. Use Docker for containerized deployment (optional).
3. Set up CI/CD pipelines for continuous integration and deployment (using GitHub Actions or other tools).

# License

This project is licensed under the MIT License.
