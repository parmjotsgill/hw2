import os
from dotenv import load_dotenv
import openai
import sounddevice as sd
import numpy as np
import soundfile as sf
from io import BytesIO

load_dotenv()
client = openai.OpenAI()

# Read text
with open("narration.txt", "r") as f:
    text = f.read()

# Generate TTS in WAV format
audio_response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=text
)

# Extract WAV bytes
wav_bytes = audio_response.content

# Read WAV data and samplerate
wav_io = BytesIO(wav_bytes)
wav_data, samplerate = sf.read(wav_io)

# Play audio
sd.play(wav_data, samplerate=samplerate)
sd.wait()