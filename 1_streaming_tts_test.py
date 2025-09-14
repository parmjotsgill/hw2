from dotenv import load_dotenv
import os
load_dotenv()  # reads .env and sets environment variables

key = os.getenv("OPENAI_API_KEY")
if key:
    # DO NOT print the key itself. Only print a harmless confirmation.
    print("✅ OPENAI_API_KEY loaded successfully (value is hidden).")
else:
    print("❌ OPENAI_API_KEY not found. Make sure .env is in the project root and contains OPENAI_API_KEY=...")

