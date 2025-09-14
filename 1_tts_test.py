
# 1_tts_test.py
import os
from dotenv import load_dotenv
import openai

# load environment variables from .env
load_dotenv()

# create OpenAI client
client = openai.OpenAI()

# request text-to-speech and save as MP3
response = client.audio.speech.create(
    model="gpt-4o-mini-tts",   # TTS model
    voice="alloy",             # choose a voice
    input="Hello, this is a text-to-speech test from Python!"  # your text
)

# save as mp3
with open("output.mp3", "wb") as f:
    f.write(response.read())
print("✅ Saved speech to output.mp3")
