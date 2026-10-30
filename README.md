# 🌍 Multilingual Question Answering System (Lab 4, early version)

An early version of a voice-enabled question answering system that answers questions about PDF documents in **English, Malayalam and French**, using Whisper for speech-to-text, FLAN-T5 for answers, and gTTS for spoken replies.

> **Note:** this repository contains the app entry points (`app.py`, `main.py`) but not the `models/`, `utils/` or `sample_docs/` folders they import. The complete, runnable project is in **[Lab4_LLM](https://github.com/Robin-Rajesh/Lab4_LLM)**.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

## 📂 Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit interface |
| `main.py` | Command-line pipeline |
| `check_pdfs.py`, `test_pdfs.py` | Helpers for checking that PDFs load |
| `Lab4instructions.pdf` | Lab brief |
| `requirements.txt` | Dependencies |
