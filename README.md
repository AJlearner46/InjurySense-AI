# 🏥 AI Medical Assessor (POC)

A **multi-agent AI system** that analyzes external injury images and produces a **medical assessment** using computer vision, medical literature, and patient-friendly communication.

---

## Features

- Vision Agent (Gemini Pro Vision)
- Diagnostic Agent (PubMed Literature Search)
- Communication Agent (Patient-friendly + Audio)
- CrewAI Multi-Agent Orchestration
- Streamlit UI
- Explainable AI Outputs

---

## System Architecture
Streamlit UI
↓
Crew Orchestrator
↓
Vision Agent → Diagnostic Agent → Communication Agent
↓
Structured Medical Assessment + Audio

---

## Setup Instructions

### 1️. Clone Repo
```bash
git clone https://github.com/.git
cd 
```

### 2️. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️. Configure Environment
```bash
cp .env
```

### 5️. Run App
```bash
streamlit run app.py
```

---

> ⚠️ **DISCLAIMER**  
> This is a proof-of-concept for educational purposes only.  
> NOT approved for clinical use. Always consult a medical professional.

---
