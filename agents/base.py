import requests

MODEL = "llama3.2:3b"
OLLAMA_URL = "http://localhost:11434/api/generate"


def call_llm(prompt: str, temperature: float = 0.3) -> str:
    """
    Call Ollama with the configured model. Returns plain text.
    """
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": temperature,
                "max_tokens": 150
            },
            timeout=90
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"


def extract_symptoms(note: str) -> str:
    prompt = f"""Read this doctor's note and list only the patient's symptoms in one short sentence. Do not include diagnosis, medications, or follow-up info.

Note: "{note}"

Symptoms:"""
    return call_llm(prompt)


def extract_diagnosis(note: str) -> str:
    prompt = f"""Read this doctor's note and state only the diagnosis (or suspected diagnosis) in a few words. Do not include symptoms, medications, or follow-up info.

Note: "{note}"

Diagnosis:"""
    return call_llm(prompt)


def extract_medications(note: str) -> str:
    prompt = f"""Read this doctor's note and list only the medications prescribed, including dosage if mentioned. Do not include symptoms, diagnosis, or follow-up info.

Note: "{note}"

Medications:"""
    return call_llm(prompt)


def extract_follow_up(note: str) -> str:
    prompt = f"""Read this doctor's note and state only the follow-up plan or instructions (timeline, tests, referrals). Do not include symptoms, diagnosis, or medications.

Note: "{note}"

Follow-up:"""
    return call_llm(prompt)