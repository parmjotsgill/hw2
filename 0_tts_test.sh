source .env
echo $OPENAI_API_KEY
source .env

PHRASE="Hello, this is a test."
MODEL="gpt-4o-mini-tts"
OUTPUT="output.mp3"

curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{
    "model": "'"$MODEL"'",
    "input": "'"$PHRASE"'"
  }' \
  --output $OUTPUT

echo "Saved speech to $OUTPUT"