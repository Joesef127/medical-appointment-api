from fastapi import APIRouter, HTTPException
from schemas.patient_schema import Patient
from service.patient_service import PatientService

patient_router = APIRouter()
patient_service = PatientService()

@patient_router.post("/patients/")
def create_patient_api(patient: Patient):
    new_patient = patient_service.create_patient(patient)
    return new_patient

@patient_router.get("/patients/{patient_id}")
def get_patient_api(patient_id: int):
    patient = patient_service.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
