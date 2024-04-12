import whisper


model = whisper.load_model('medium.en')
result = model.transcribe('mis/s11.mp3',fp16=False)

print(result['text'])


