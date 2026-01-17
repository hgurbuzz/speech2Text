import whisper
import requests
import json
import os

# -----------------------
# AYARLAR
# -----------------------
AUDIO_FILE = r"C:\Users\hakan\Downloads\Medya3.wav"
TXT_FILE = "transcript.txt"

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:latest"   # isterse değiştir
LANGUAGE = "tr"

# -----------------------
# 1️⃣ WHISPER TRANSCRIBE
# -----------------------
print("🎧 Whisper transcribe başlıyor...")

model = whisper.load_model("large")
result = model.transcribe(AUDIO_FILE, language=LANGUAGE, fp16=False)

text = result["text"]

with open(TXT_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Transkript yazıldı:", TXT_FILE)

# -----------------------
# 2️⃣ OLLAMA PROMPT
# -----------------------
prompt = f"""
Aşağıda bir toplantı / konuşma dökümü bulunmaktadır.

Bu metni analiz et ve:
- Sadece alınan kararları çıkar
- Her kararı kısa ve net maddeler halinde yaz
- Gereksiz açıklama yapma

Metin:
\"\"\"
{text}
\"\"\"

Çıktı formatı:
1. ...
2. ...
"""

# -----------------------
# 3️⃣ OLLAMA'YA GÖNDER
# -----------------------
print("🧠 Ollama özet çıkarıyor...")

response = requests.post(
    OLLAMA_URL,
    json={
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    },
    timeout=300
)

response.raise_for_status()

result = response.json()["response"]

# -----------------------
# 4️⃣ SONUÇ
# -----------------------
print("\n📌 KARAR MADDELERİ:\n")
print(result)
