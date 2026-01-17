import whisper
import os

audio = r"C:\Users\hakan\Downloads\Medya2.wav"

assert os.path.exists(audio), "Ses dosyası bulunamadı!"

model = whisper.load_model("large")  # önce small
result = model.transcribe(audio, language="tr", fp16=False)

print(result["text"])
