import os
from dotenv import load_dotenv
import openai
import sounddevice as sd
import numpy as np
import wave

load_dotenv()
client = openai.OpenAI()

# List of voices to try
voices = ["alloy", "aria", "classic"]

# List of effects to apply
effects = ["normal", "faster", "slower", "higher_pitch", "lower_pitch"]

# Read your text
with open("narration.txt", "r") as f:
    text = f.read()

# Function to apply simple effects to raw WAV data
def apply_effect(wav_data, effect):
    data = wav_data.astype(np.float32)  # convert to float for processing
    if effect == "faster":
        data = np.interp(np.arange(0, len(data), 0.8), np.arange(len(data)), data)
    elif effect == "slower":
        data = np.interp(np.arange(0, len(data), 1.2), np.arange(len(data)), data)
    elif effect == "higher_pitch":
        data = np.interp(np.arange(0, len(data), 0.9), np.arange(len(data)), data)
    elif effect == "lower_pitch":
        data = np.interp(np.arange(0, len(data), 1.1), np.arange(len(data)), data)
    return data.astype(np.int16)

# Cycle through voices and effects
for voice in voices:
    for effect in effects:
        print(f"Generating voice={voice}, effect={effect}...")

        # Generate TTS from OpenAI
        audio_response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice=voice,
            input=text
        )
        audio_bytes = audio_response.read()
        wav_data = np.frombuffer(audio_bytes, dtype=np.int16)

        # Apply effect
        wav_data = apply_effect(wav_data, effect)

        # Save to WAV file
        filename = f"narration_{voice}_{effect}.wav"
        with wave.open(filename, 'w') as wf:
            wf.setnchannels(1)  # mono
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(22050)
            wf.writeframes(wav_data.tobytes())

        # Play the audio
        sd.play(wav_data, samplerate=22050)
        sd.wait()