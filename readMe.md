# Medical Appointment API

This is a simple API for managing medical appointments between patients and doctors.

## Features

- CRUD endpoints for managing patients
- CRUD endpoints for managing doctors
- Endpoint for creating appointments
- Endpoint for completing appointments
- Endpoint for canceling appointments
- Endpoint for setting availability status for doctors

## Technologies Used

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Pydantic: Data validation library for Python.
- Uvicorn: ASGI server for running FastAPI applications.

## Installation

1. Clone the repository:
https://github.com/joesef127/medical-appointment-api.git

2. Install dependencies:
pip install -r requirements.txt

## Usage

1. Run the server:
uvicorn main:app --reload

2. Open your web browser and navigate to `http://localhost:8000/docs` to view the interactive API documentation.

3. Send requests to the API endpoints.

## API Endpoints

- **POST /patients/**: Create a new patient.
- **GET /patients/{patient_id}**: Get details of a specific patient.
- **POST /doctors/**: Create a new doctor.
- **GET /doctors/{doctor_id}**: Get details of a specific doctor.
- **PUT /doctors/{doctor_id}/availability/**: Set doctor availability status.
- **POST /appointments/**: Create a new appointment.
- **PUT /appointments/{appointment_id}/complete/**: Complete an appointment.
- **PUT /appointments/{appointment_id}/cancel/**: Cancel an appointment.

