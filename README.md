<div align="center">

# MedStruct-AI

### Structured clinical documentation from unstructured notes, powered by a local LLM.

Note to Chart takes a doctor's free-text clinical note and extracts symptoms, diagnosis, medications, and follow-up into clean, structured fields. It runs entirely on a local Ollama model, with a FastAPI backend and a Flask-based frontend.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Flask](https://img.shields.io/badge/Flask-Frontend-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?logo=ollama&logoColor=white)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

</div>

---

## Demo

<div align="center">

<img width="1252" height="837" alt="Image" src="https://github.com/user-attachments/assets/8d610ee8-656b-4e23-a840-16db8a23a7a4" />

<img width="1407" height="835" alt="Image" src="https://github.com/user-attachments/assets/0b30c339-7845-4a4b-9d48-84758f852880" />

</div>

---


## Overview

Clinical notes are typically written as free-flowing paragraphs rather than structured data. Note to Chart reads an already-written doctor's note and reorganizes the information it already contains into four defined fields:

- Symptoms
- Diagnosis
- Medications
- Follow-up

This is a documentation and structuring tool, not a diagnostic one. It extracts information a clinician has already recorded rather than suggesting a diagnosis from patient-reported symptoms.

---

## Features

- Single-call structured extraction using a JSON-constrained prompt for speed and consistency
- Local-first: runs entirely against a self-hosted Ollama model, with no external API calls
- Clean separation of concerns between extraction logic, API layer, and UI
- Downloadable extraction results in JSON format
- Graceful fallback if the model returns malformed output, so a request never crashes

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM runtime | Ollama (local) |
| Backend API | FastAPI |
| Frontend | Flask, HTML, CSS, JavaScript |
| Language | Python 3.10+ |

---

## Project Structure

```
medical_notes_flask/
├── main.py                 # FastAPI backend — /extract/ endpoint
├── agents/
│   ├── __init__.py
│   └── base.py              # LLM prompt and extraction logic
├── flask_app.py             # Flask server — serves the UI, proxies to FastAPI
├── templates/
│   └── index.html
├── static/
│   ├── css/style.css
│   └── js/script.js
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Ollama installed and running locally
- A pulled Ollama model (default: `qwen3:8b`, configurable in `agents/base.py`)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd medical_notes_flask

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull an Ollama model (if not already installed)
ollama pull qwen3:8b
```

### Running

This project runs as two processes:

```bash
# Terminal 1 — start the backend
uvicorn main:app --port 8000

# Terminal 2 — start the frontend
python flask_app.py
```

Then open `http://localhost:5000` in a browser.

---

## Usage

1. Paste a clinical note into the text area, or use the provided sample note.
2. Click "Structure this note."
3. Review the extracted fields, presented as a structured chart entry.
4. Optionally download the result as a JSON file.


---

## Roadmap

- Support batch note uploads
- Add confidence indicators per extracted field
- Export to structured formats beyond JSON, such as FHIR

---

## License

This project is licensed under the MIT License.

---

<div align="center">

Built by Esha Mirza — [GitHub](https://github.com/Esha-Mirza) · [LinkedIn](https://linkedin.com/in/esha-mirza1623)

</div>

---

<p align="center">
  <strong>MedStruct-AI</strong><br>
  Note to Chart
</p>
