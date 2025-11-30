🧠 AI NLP Playground

A modern, clean, and powerful multi-tool Natural Language Processing web application built using Python + Streamlit.
This project integrates several NLP features—sentiment analysis, summarization, keyword extraction, translation, PDF summarization, fake-news detection, and a chatbot—into a single, lightweight platform.

🚀 Features
✔ 1. Sentiment Analysis

Uses TextBlob to detect if a sentence is Positive, Negative, or Neutral.

✔ 2. Text Summarization

Powered by LexRank (SUMY library) for extractive summarization of long text.

✔ 3. Keyword Extraction

Uses RAKE (Rapid Automatic Keyword Extraction) to extract the most important keywords.

✔ 4. Fake News Detector

A lightweight rule-based model that detects misleading or sensational content.

✔ 5. Chatbot Assistant

A simple, rule-based assistant that replies to common queries.

✔ 6. Language Translation

Uses Deep Translator (Google Translator API wrapper) to translate:

English → Hindi

Hindi → English

✔ 7. PDF → Text Summarization

Extracts text from uploaded PDFs using PyPDF2 and generates a clean summary.

✔ 8. Modern UI with Custom CSS

Dark theme

Gradient headings

Styled radio buttons

Smooth hover animations

Clean layout

🛠️ Technologies Used
Component	Technology
UI Framework	Streamlit
Sentiment Analysis	TextBlob
Summarization	SUMY – LexRank Algorithm
Keyword Extraction	RAKE (NLTK)
Translation	deep-translator
PDF Extraction	PyPDF2
Stopwords	NLTK
Styling	Custom CSS (Google Poppins font)
📂 Project Structure
AI-NLP-Playground/
│
├── app.py             # Main Streamlit app
├── README.md          # Documentation
├── requirements.txt   # All dependencies


📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/AI-NLP-Playground.git
cd AI-NLP-Playground

2️⃣ Install dependencies

Create a virtual environment (recommended):

pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py

📘 Usage Guide

Choose any tool from the sidebar:

Enter text (or upload PDF)

Click the action button

Get instant output in real time

The UI is clean and responsive.

📜 How the Main Modules Work
🔹 LexRank Summarization

A graph-based algorithm similar to Google PageRank:

Sentences → vectors

Graph → built using similarity scores

Top-ranked sentences → summary

🔹 RAKE Keyword Extraction

Removes stopwords

Finds phrase patterns

Ranks them by frequency & importance

🔹 Sentiment Analysis (TextBlob)

Uses pre-trained pattern models

Returns a polarity score

🔹 Translation

Uses Google Neural Machine Translation (NMT)

Works without any API key using Deep Translator

🧪 Sample Commands
generate_summary("your long text here")
translate_text("Hello world", "English → Hindi")



🎯 Future Improvements

Add Hugging Face Transformer-based models

Add OCR support

Add speech-to-text and text-to-speech

Add database for conversation history

🤝 Contributing

Pull requests are welcome!
If you want to suggest improvements:

Fork the repository

Create a new branch

Commit changes

Submit a PR

📜 License

This project is open-source and available under the MIT License.

⭐ Support

If you like this project, please ⭐ star the repository on GitHub!