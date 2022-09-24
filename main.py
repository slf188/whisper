import whisper

model = whisper.load_model("base")
result = model.transcribe("portuguese.m4a")
print(result["text"])
