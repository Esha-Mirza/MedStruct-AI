from fastapi import FastAPI, Form
from concurrent.futures import ThreadPoolExecutor
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.base import extract_symptoms, extract_diagnosis, extract_medications, extract_follow_up

app = FastAPI(title="Medical Note Structuring", version="1.0.0")

# Each extract_* call hits Ollama independently, so they don't need to
# wait on each other. Running them in a small thread pool means total
# time is roughly the slowest single call, not the sum of all four.
executor = ThreadPoolExecutor(max_workers=4)


@app.get("/")
def root():
    return {"message": "Medical Note Structuring API"}


@app.post("/extract/")
def extract_medical(note: str = Form(...)):
    future_symptoms = executor.submit(extract_symptoms, note)
    future_diagnosis = executor.submit(extract_diagnosis, note)
    future_medications = executor.submit(extract_medications, note)
    future_follow_up = executor.submit(extract_follow_up, note)

    symptoms = future_symptoms.result()
    diagnosis = future_diagnosis.result()
    medications = future_medications.result()
    follow_up = future_follow_up.result()

    print("SYMPTOMS:", symptoms)
    print("DIAGNOSIS:", diagnosis)
    print("MEDICATIONS:", medications)
    print("FOLLOW-UP:", follow_up)

    result = {
        "symptoms": symptoms,
        "diagnosis": diagnosis,
        "medications": medications,
        "follow_up": follow_up
    }

    return {"structured": result}