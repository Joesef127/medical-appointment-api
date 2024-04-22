from fastapi import APIRouter, HTTPException
from schemas.doctors_schema import Doctor
from service.doctor_service import DoctorService

doctor_router = APIRouter()
doctor_service = DoctorService()

@doctor_router.post("/doctors/")
def create_doctor_api(doctor: Doctor):
    new_doctor = doctor_service.create_doctor(doctor)
    return new_doctor

@doctor_router.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor_api(doctor_id: int):
    doctor = doctor_service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@doctor_router.put("/doctors/{doctor_id}/availability/")
def set_doctor_availability_api(doctor_id: int, is_available: bool):
    doctor_service.set_doctor_availability(doctor_id, is_available)
