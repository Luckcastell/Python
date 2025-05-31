import whisper

# Cargar el modelo
model = whisper.load_model("base")

# Transcribir el archivo de audio
result = model.transcribe("Grabación.mp3")

# Imprimir el texto transcrito
print(f'Texto transcrito: \n{result["text"]}')

# Python transcribe.py