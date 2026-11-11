import streamlit as st
from vennila import synthesize, DEFAULT_MODEL, FALLBACK_MODEL

st.set_page_config(page_title="Vennila Voice Studio", page_icon="🎙️")
st.title("🎙️ Vennila Voice Studio")
st.caption("Tamil conversational voice via ElevenLabs")

with st.sidebar:
    api_key = st.text_input("ElevenLabs API key", type="password",
                            help="Or set the ELEVENLABS_API_KEY env var.")
    model_id = st.selectbox("Model", [DEFAULT_MODEL, FALLBACK_MODEL])
    custom = st.text_input("Custom model ID (optional)")
    stability = st.slider("Stability", 0.0, 1.0, 0.5, 0.05,
                          help="Lower = more expressive, higher = more consistent")
    similarity = st.slider("Similarity boost", 0.0, 1.0, 0.75, 0.05)
    st.markdown("**Tip:** with `eleven_v3` you can add tags like "
                "`[whispers]`, `[giggles]`, `[sarcastically]`.")

PRESETS = {
    "Greeting": "வணக்கம்! இன்னைக்கு நாள் எப்படி போச்சு?",
    "Late-night check-in": "[whispers] இன்னும் தூங்கலயா? கொஞ்சம் ஓய்வு எடுத்துக்கோங்க.",
    "Story": "பண்டைய எல்டோரியா நாட்டில், ஒரு டிராகன் வாழ்ந்தான். [whispers] அவன் சென்றபோது பறவைகளும் அமைதியாக இருந்தன.",
}
choice = st.selectbox("Preset", ["Custom"] + list(PRESETS))
text = st.text_area("Text", value=PRESETS.get(choice, ""), height=160)

if st.button("Generate", type="primary", disabled=not text.strip()):
    try:
        with st.spinner("Generating..."):
            audio = synthesize(text, api_key=api_key or None,
                               model_id=custom.strip() or model_id,
                               stability=stability, similarity_boost=similarity)
        st.audio(audio, format="audio/mp3")
        st.download_button("Download MP3", audio, "vennila.mp3", "audio/mpeg")
    except Exception as e:
        st.error(str(e))
