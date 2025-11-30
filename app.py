import streamlit as st
from textblob import TextBlob
from rake_nltk import Rake
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import PyPDF2
from deep_translator import GoogleTranslator       # FIXED TRANSLATOR

nltk.download("stopwords")

# =====================================================
#   CSS STYLES (your original code)
# =====================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body {
    font-family: 'Poppins', sans-serif !important;
}

/* ------------------------------------------------ */
/*              GLOBAL PAGE STYLING                 */
/* ------------------------------------------------ */

.block-container {
    padding-top: 2rem !important;
}

body {
    background: radial-gradient(circle at top, #1c1c24, #0e0e14);
    color: #fff;
}

/* Main Title */
.app-title {
    font-size: 50px;
    text-align: center;
    font-weight: 800;
    margin-top: 20px;
    background: linear-gradient(90deg, #4facfe, #00f2fe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 0px 20px rgba(79, 172, 254, 0.4);
}

/* Section Titles */
.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 15px;
    background: linear-gradient(90deg, #43e97b, #38f9d7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ------------------------------------------------ */
/*                SIDEBAR UPGRADE                   */
/* ------------------------------------------------ */

section[data-testid="stSidebar"] {
    background: rgba(18, 18, 28, 0.8) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}

.stRadio > div {
    gap: 12px !important;
    flex-direction: column;
}

/* Sidebar Buttons */
.stRadio label {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 14px !important;
    padding: 14px 18px !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    width: 100%;
    color: #f2f2f2 !important;
    transition: all 0.25s ease-in-out;
    font-size: 17px !important;
}

.stRadio label:hover {
    background: rgba(255,255,255,0.12) !important;
    transform: translateX(4px) scale(1.03);
}

.stRadio [aria-checked="true"] > label {
    background: linear-gradient(120deg, #6a5af9, #865dff) !important;
    border-color: transparent !important;
    color: white !important;
    font-weight: 700;
    transform: translateX(6px) scale(1.05);
}

/* ------------------------------------------------ */
/*               TEXT AREA STYLING                  */
/* ------------------------------------------------ */

textarea {
    background: rgba(255,255,255,0.07) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
    padding: 14px !important;
}

textarea:focus {
    border-color: #6a5af9 !important;
    box-shadow: 0 0 10px #6a5af9 !important;
}

/* ------------------------------------------------ */
/*               BUTTON UPGRADE                     */
/* ------------------------------------------------ */

.stButton > button {
    background: linear-gradient(120deg, #6a5af9, #865dff);
    color: white;
    padding: 12px 25px;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    font-weight: 600;
    transition: 0.25s ease-in-out;
}

.stButton > button:hover {
    transform: scale(1.07);
    box-shadow: 0px 0px 18px rgba(138, 92, 255, 0.6);
}

/* ------------------------------------------------ */
/*              SUCCESS / ERROR BOXES               */
/* ------------------------------------------------ */

.stSuccess {
    background: rgba(0, 255, 127, 0.1) !important;
    border-left: 4px solid #00ff95 !important;
}

.stError {
    background: rgba(255, 0, 76, 0.12) !important;
    border-left: 4px solid #ff4d6d !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
#   TEXT SUMMARIZER
# =====================================================
def generate_summary(text, sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences)
    return " ".join(str(sentence) for sentence in summary)


# =====================================================
#   TRANSLATOR (NOW USING deep-translator)
# =====================================================
def translate_text(text, direction):
    try:
        if direction == "English → Hindi":
            return GoogleTranslator(source='en', target='hi').translate(text)
        else:
            return GoogleTranslator(source='hi', target='en').translate(text)
    except Exception as e:
        return f"Translation Error: {e}"


# =====================================================
#   PDF READER
# =====================================================
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


# =====================================================
#   MAIN UI HEADER
# =====================================================
st.markdown("<div class='app-title'>🤖 AI NLP Playground</div>", unsafe_allow_html=True)
st.write("A refined & modern NLP toolkit — clean, fast, powerful.")


# =====================================================
#   SIDEBAR MENU
# =====================================================
menu = st.sidebar.radio(
    "Choose a tool",
    [
        "🧩 Sentiment Analysis",
        "📰 Text Summarization",
        "🗝 Keyword Extraction",
        "🚨 Fake News Detector",
        "💬 Chatbot",
        "🌍 Translation",
        "📄 PDF → Summarizer"
    ]
)

# =====================================================
#   SENTIMENT ANALYSIS
# =====================================================
if menu == "🧩 Sentiment Analysis":
    st.markdown("<div class='section-title'>🧩 Sentiment Analysis</div>", unsafe_allow_html=True)
    text = st.text_area("Enter text:")

    if st.button("Analyze Sentiment"):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            st.success("🙂 Positive Sentiment")
        elif polarity < 0:
            st.error("☹ Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")


# =====================================================
#   TEXT SUMMARIZATION
# =====================================================
elif menu == "📰 Text Summarization":
    st.markdown("<div class='section-title'>📰 Text Summarization</div>", unsafe_allow_html=True)
    text = st.text_area("Paste your text below:")

    if st.button("Generate Summary"):
        if len(text.split()) < 40:
            st.warning("Enter at least 40+ words for a meaningful summary.")
        else:
            summary = generate_summary(text)
            st.info(summary)


# =====================================================
#   KEYWORD EXTRACTION
# =====================================================
elif menu == "🗝 Keyword Extraction":
    st.markdown("<div class='section-title'>🗝 Keyword Extraction</div>", unsafe_allow_html=True)
    text = st.text_area("Enter text to extract keywords:")

    if st.button("Extract"):
        r = Rake()
        r.extract_keywords_from_text(text)
        keywords = r.get_ranked_phrases()[:10]

        st.success("Top Keywords:")
        for kw in keywords:
            st.write("🔹", kw)


# =====================================================
#   FAKE NEWS DETECTOR
# =====================================================
elif menu == "🚨 Fake News Detector":
    st.markdown("<div class='section-title'>🚨 Fake News Detector</div>", unsafe_allow_html=True)
    text = st.text_area("Enter news content:")

    if st.button("Check"):
        fake_words = ["shocking", "viral", "guaranteed", "breaking", "urgent"]
        score = sum(1 for w in fake_words if w in text.lower())

        if score >= 2:
            st.error("⚠ This looks like Fake News!")
        else:
            st.success("✔ This appears to be Real News.")


# =====================================================
#   CHATBOT
# =====================================================
elif menu == "💬 Chatbot":
    st.markdown("<div class='section-title'>💬 Chatbot Assistant</div>", unsafe_allow_html=True)
    user = st.text_input("You:")

    if st.button("Ask"):
        responses = {
            "hello": "Hi! How can I assist you today?",
            "hi": "Hello! 😊",
            "what is nlp": "NLP means Natural Language Processing.",
            "who are you": "I am your NLP assistant!",
            "bye": "Goodbye! 👋"
        }
        st.write("🤖", responses.get(user.lower(), "I am still learning new things! 😊"))


# =====================================================
#   TRANSLATION (fixed)
# =====================================================
elif menu == "🌍 Translation":
    st.markdown("<div class='section-title'>🌍 Language Translation</div>", unsafe_allow_html=True)
    text = st.text_area("Enter text:")
    direction = st.radio("Direction", ["English → Hindi", "Hindi → English"])

    if st.button("Translate"):
        output = translate_text(text, direction)
        st.success(output)


# =====================================================
#   PDF → SUMMARY
# =====================================================
elif menu == "📄 PDF → Summarizer":
    st.markdown("<div class='section-title'>📄 PDF → Text Summary</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF loaded successfully!")

        if st.button("Summarize PDF"):
            summary = generate_summary(pdf_text, sentences=4)
            st.info(summary)