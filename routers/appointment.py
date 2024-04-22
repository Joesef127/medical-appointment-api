from fastapi import APIRouter, HTTPException
from schemas.appointment_schema import Appointment
from service.appointment_service import AppointmentService

appointment_router = APIRouter()
appointment_service = AppointmentService()

@appointment_router.post("/appointments/")
def create_appointment_api(appointment: Appointment):
    new_appointment = appointment_service.create_appointment(appointment)
    return new_appointment

@appointment_router.put("/appointments/{appointment_id}/complete/")
def complete_appointment_api(appointment_id: int):
    appointment_service.complete_appointment(appointment_id)

@appointment_router.put("/appointments/{appointment_id}/cancel/")
def cancel_appointment_api(appointment_id: int):
    appointment_service.cancel_appointment(appointment_id)
