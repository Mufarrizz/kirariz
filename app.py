import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="KIRARIZ Translator",
    page_icon="🌸",
    layout="centered"
)

# -------------------- FORCE LIGHT THEME + COLORS --------------------
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #ffe6f0;
        color: black;
    }

    /* Titles & labels */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: black !important;
    }

    /* Selectbox + Textarea */
    div[data-baseweb="select"] > div {
        background-color: #ffd6e8 !important;
        color: black !important;
    }

    textarea {
        background-color: #ffd6e8 !important;
        color: black !important;
    }

    /* Dropdown text */
    li {
        color: black !important;
    }

    /* Buttons */
    button {
        background-color: #ffb6d5 !important;
        color: black !important;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- SESSION STATE --------------------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# -------------------- TITLE --------------------
st.markdown(
    "<h1 style='text-align:center;'>🌍 KIRARIZ Translator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>API & JSON based Language Translator</p>",
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
    st.markdown("### Translated Text")

    st.markdown(
        f"""
        <div style="
            background-color:#ffd6e8;
            padding:18px;
            border-radius:12px;
            font-size:20px;
            color:black;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
        ">
            {st.session_state.translated_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='margin-top:10px; font-size:14px;'>🎤 Voice feature coming soon</p>",
        unsafe_allow_html=True
    )

# -------------------- FOOTER --------------------
st.markdown("---")

st.markdown(
    "<p style='text-align:center; font-size:12px;'>KIRARIZ • School Exhibition Project</p>",
    unsafe_allow_html=True
)
