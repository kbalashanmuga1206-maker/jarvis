# Vennila Voice Studio

Small Streamlit app + CLI for the ElevenLabs **Vennila** Tamil voice (`IypOXKDlkcNuR6IFgGCU`).

## Run
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY=your_key     # Windows: set ELEVENLABS_API_KEY=your_key
streamlit run app.py                   # web UI
python cli.py "வணக்கம்!" -o hello.mp3  # command line
```

## Files
- `vennila.py` – API client (`synthesize()`), reusable in other projects
- `app.py` – Streamlit UI (presets, model/stability controls, download)
- `cli.py` – one-shot command line TTS

## Notes
- `eleven_v3` supports expressive tags (`[whispers]`, `[giggles]`); `eleven_multilingual_v2` does not.
- Use the "Custom model ID" box if ElevenLabs' newer v4 model has a different ID.
