import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.set_page_config(page_title="AI Language Translator", page_icon="🌍", layout="centered")

# 🎨 CLEAN UI CSS (spacing fixed)
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef2f3, #d9e4f5);
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: white;
    background: linear-gradient(90deg, #4a90e2, #1f3c88);
    padding: 10px;
    border-radius: 12px;
    margin-bottom: 5px;
}

/* Subtitle */
.sub {
    text-align: center;
    color: #444;
    font-size: 14px;
    margin-bottom: 5px;
}

/* Labels */
.label {
    font-size: 15px;
    font-weight: 600;
    color: #1f3c88;
    margin-bottom: 2px;   /* 🔥 reduced spacing */
    margin-top: 2px;      /* 🔥 reduced spacing */
}

/* Text area */
.stTextArea textarea {
    border: 2px solid #4a90e2;
    border-radius: 10px;
}

/* Select box */
.stSelectbox div {
    border-radius: 8px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #1f3c88, #4a90e2);
    color: white;
    font-size: 17px;
    padding: 8px;
    border-radius: 10px;
    width: 100%;
}

.stButton>button:hover {
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# 🏷️ TITLE
st.markdown("<div class='title'>🌍 AI LANGUAGE TRANSLATOR</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Translate • Copy • Speak instantly</div>", unsafe_allow_html=True)

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja"
}

lang_list = list(languages.keys())

# 📌 TEXT INPUT (tight spacing)
st.markdown("<div class='label'>Enter Text</div>", unsafe_allow_html=True)
text = st.text_area("", height=90)   # 🔥 reduced height

# 🌐 LANGUAGE SELECT (tight layout)
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='label'>From Language</div>", unsafe_allow_html=True)
    source = st.selectbox("", lang_list, index=1)

with col2:
    st.markdown("<div class='label'>To Language</div>", unsafe_allow_html=True)
    target = st.selectbox("", lang_list, index=3)

# SESSION
if "result" not in st.session_state:
    st.session_state.result = ""

# TRANSLATE
if st.button("🚀 Translate"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        st.session_state.result = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

# OUTPUT
if st.session_state.result:

    st.success("Translated Text")

    st.markdown(f"""
    <div style="
        font-size:20px;
        color:#1f3c88;
        font-weight:bold;
        background:white;
        padding:10px;
        border-radius:10px;
        border-left:5px solid #4a90e2;">
        {st.session_state.result}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📋 Copy"):
            st.code(st.session_state.result)

    with col2:
        if st.button("🔊 Speak"):
            tts = gTTS(text=st.session_state.result, lang='en')
            tts.save("voice.mp3")
            st.audio("voice.mp3")