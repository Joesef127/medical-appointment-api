from typing import List
from schemas.patient_schema import Patient

class PatientService:
    def __init__(self):
        self.patients: List[Patient] = []

    def create_patient(self, patient: Patient) -> Patient:
        if self.get_patient(patient.id):
            raise HTTPException(status_code=400, detail="Patient ID already exists")
        self.patients.append(patient)
        return patient

    def get_patient(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None
