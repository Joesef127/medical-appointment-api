from fastapi import FastAPI

from routers.patient import patient_router
from routers.doctor import doctor_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(patient_router, prefix="/Patient", tags=["Patients"])

app.include_router(doctor_router, prefix="/Doctor", tags=["Doctors"])

app.include_router(appointment_router, prefix="/Appointment", tags=["Appointment"])



@app.get("/")
def home():
  return "Welcome user!"