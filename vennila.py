"""Thin ElevenLabs client for the Vennila Tamil voice."""
import os
import requests

VOICE_ID = "IypOXKDlkcNuR6IFgGCU"  # Vennila
API_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
DEFAULT_MODEL = "eleven_v3"  # supports [whispers], [giggles] style tags
FALLBACK_MODEL = "eleven_multilingual_v2"  # no audio tags, very stable for Tamil


def synthesize(
    text: str,
    api_key: str | None = None,
    model_id: str = DEFAULT_MODEL,
    voice_id: str = VOICE_ID,
    stability: float = 0.5,
    similarity_boost: float = 0.75,
    output_format: str = "mp3_44100_128",
) -> bytes:
    """Return MP3 bytes for `text` spoken in Vennila's voice."""
    api_key = api_key or os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("Set ELEVENLABS_API_KEY or pass api_key.")
    resp = requests.post(
        API_URL.format(voice_id=voice_id),
        params={"output_format": output_format},
        headers={"xi-api-key": api_key, "Content-Type": "application/json"},
        json={
            "text": text,
            "model_id": model_id,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
            },
        },
        timeout=60,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"ElevenLabs error {resp.status_code}: {resp.text[:300]}")
    return resp.content
