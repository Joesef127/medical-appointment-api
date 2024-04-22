from typing import List
from schemas.doctors_schema import Doctor

class DoctorService:
    def __init__(self):
        self.doctors: List[Doctor] = []

    def create_doctor(self, doctor: Doctor) -> Doctor:
        if self.get_doctor(doctor.id):
            raise HTTPException(status_code=400, detail="Doctor ID already exists")
        self.doctors.append(doctor)
        return doctor

    def get_doctor(self, doctor_id: int) -> Doctor:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def set_doctor_availability(self, doctor_id: int, is_available: bool):
        doctor = self.get_doctor(doctor_id)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctor.is_available = is_available
