from typing import List
from schemas.appointment_schema import Appointment
from service.doctor_service import DoctorService
from service.patient_service import PatientService
from datetime import datetime
from fastapi import HTTPException

class AppointmentService:
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.doctor_service = DoctorService()
        self.patient_service = PatientService()

    def create_appointment(self, appointment: Appointment) -> Appointment:
        # Check if the doctor is available
        doctor = self.doctor_service.get_doctor(appointment.doctor)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        if not doctor.is_available:
            raise HTTPException(status_code=400, detail="Doctor is not available")

        # Check if the patient exists
        patient = self.patient_service.get_patient(appointment.patient)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")

        # Check if the appointment date is in the future
        appointment_date = datetime.strptime(appointment.date, "%Y-%m-%d")
        current_date = datetime.now()
        if appointment_date <= current_date:
            raise HTTPException(status_code=400, detail="Appointment date must be in the future")

        self.appointments.append(appointment)
        return appointment

    def complete_appointment(self, appointment_id: int):
        appointment = self.get_appointment(appointment_id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        # Mark the appointment as completed
        appointment.is_completed = True

    def cancel_appointment(self, appointment_id: int):
        appointment = self.get_appointment(appointment_id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        # Remove the appointment from the list
        self.appointments.remove(appointment)

    def get_appointment(self, appointment_id: int) -> Appointment:
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                return appointment
        return None
