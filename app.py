import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="KIRARIZ Translator",
    page_icon="🌸",
    layout="centered"
)

# -------------------- GLOBAL STYLES (FIX DARK MODE ISSUE) --------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0;
    }

    /* Text input & text area */
    textarea, input {
        background-color: #ffd6e8 !important;
        color: #000000 !important;
        border-radius: 10px !important;
        border: 1px solid #ff9fc9 !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: #ffd6e8 !important;
        color: black !important;
        border-radius: 10px !important;
        border: 1px solid #ff9fc9 !important;
    }

    /* Dropdown text */
    div[data-baseweb="select"] span {
        color: black !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #ff9fc9;
        color: black;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
    }

    .stButton > button:hover {
        background-color: #ff7fb3;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- SESSION STATE --------------------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# -------------------- TITLE --------------------
st.markdown("<h1 style='text-align:center;'>🌍 KIRARIZ Translator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#555;'>Simple Language Translator • Exhibition Demo</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# -------------------- LANGUAGE OPTIONS --------------------
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys()),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(LANGUAGES.keys()),
        index=1
    )

# -------------------- INPUT TEXT --------------------
input_text = st.text_area(
    "Enter text to translate",
    height=120,
    placeholder="Type something here..."
)

# -------------------- TRANSLATION FUNCTION --------------------
def translate_text(text, src, tgt):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{src}|{tgt}"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["responseData"]["translatedText"]

# -------------------- TRANSLATE BUTTON --------------------
if st.button("🔁 Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        st.session_state.translated_text = translate_text(
            input_text,
            LANGUAGES[source_lang],
            LANGUAGES[target_lang]
        )

# -------------------- OUTPUT --------------------
if st.session_state.translated_text:
    st.markdown("### ✨ Translated Text")

    st.markdown(
        f"""
        <div style="
            background-color:#ffd6e8;
            padding:18px;
            border-radius:12px;
            font-size:20px;
            color:#000;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
        ">
            {st.session_state.translated_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='margin-top:10px; color:#777;'>🔊 Voice feature coming soon</p>",
        unsafe_allow_html=True
    )

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:12px;'>KIRARIZ • School Exhibition Project</p>",
    unsafe_allow_html=True
)
