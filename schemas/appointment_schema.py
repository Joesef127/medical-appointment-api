from pydantic import BaseModel
from schemas.doctors_schema import Doctor
from schemas.patient_schema import Patient

class Appointment(BaseModel):
    id: int
    patient: int
    doctor: int
    date: str
    is_completed: bool = False
