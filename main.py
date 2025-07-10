from utils.pdf_utils import extract_text_from_pdf
from utils.stt import transcribe_audio
from utils.tts import speak

from models.english_qa import answer_english
from models.indic_qa import answer_malayalam
from models.international_qa import answer_french

# Step 1: Load PDF content
eng_text = extract_text_from_pdf("sample_docs/english solar.pdf")
ml_text = extract_text_from_pdf("sample_docs/malayalam solar.pdf")
fr_text = extract_text_from_pdf("sample_docs/french solar.pdf")

# Step 2: Get voice input (from question.wav) or text input
import os
if os.path.exists("question.wav"):
    print("\n🔊 Transcribing voice question...")
    question = transcribe_audio("question.wav")
    print("📥 Transcribed Question:", question)
else:
    print("\n❓ No question.wav found. Please enter your question:")
    question = input("Your question: ")
    print("📥 Question:", question)

# Step 3: Answer in English
print("\n🧠 Answering in English...")
eng_answer = answer_english(question, eng_text)
print("✅ English Answer:", eng_answer)
audio_file = speak(eng_answer, lang='en', filename='english_answer.mp3')
if audio_file:
    print("🎵 English audio saved as:", audio_file)

# Step 4: Answer in Malayalam
print("\n🧠 Answering in Malayalam...")
ml_answer = answer_malayalam(question, ml_text)
print("✅ Malayalam Answer:", ml_answer)
audio_file = speak(ml_answer, lang='ml', filename='malayalam_answer.mp3')
if audio_file:
    print("🎵 Malayalam audio saved as:", audio_file)

# Step 5: Answer in French
print("\n🧠 Answering in French...")
fr_answer = answer_french(question, fr_text)
print("✅ French Answer:", fr_answer)
audio_file = speak(fr_answer, lang='fr', filename='french_answer.mp3')
if audio_file:
    print("🎵 French audio saved as:", audio_file)
