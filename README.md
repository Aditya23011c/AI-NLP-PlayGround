# AI-NLP-PlayGround

🧠 AI NLP Playground
A Modern Multi-Tool Natural Language Processing Web App Built with Streamlit
<div align="center"> <img src="assets/logo.png" width="160">










</div>
📌 Overview

AI NLP Playground is an interactive, lightweight, and easy-to-use Natural Language Processing toolkit built with Streamlit.
It combines multiple NLP utilities into a single interface, making it perfect for:

Students

Researchers

Developers

Educators

Anyone exploring NLP concepts

This project demonstrates real-world NLP techniques such as sentiment analysis, summarization, translation, keyword extraction, and more — using popular Python NLP libraries.

🚀 Features
Feature	Description
🧩 Sentiment Analysis	Classifies text as Positive, Negative, or Neutral
📰 Text Summarization	SUMY LexRank-based fast & lightweight summary
🗝 Keyword Extraction	Extracts top keywords using RAKE
🚨 Fake News Detection	Rule-based analyzer to detect misleading content
💬 Chatbot	Predefined conversational assistant
🌍 English ↔ Hindi Translation	Accurate translation using deep-translator
📄 PDF Summarizer	Upload PDF → extract text → get summary
🏗 Project Architecture
AI NLP Playground/
│── app.py
│── requirements.txt
│── README.md
│── assets/
│     └── logo.png
│     └── screenshots/
│── sample_pdfs/
│── .gitignore
└── …

⭐ Demo Preview (Optional GIF)

You can add a demo GIF here:

![Demo](assets/demo.gif)

🔧 Installation Guide
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-NLP-PlayGround.git
cd AI-NLP-PlayGround

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run app.py

💡 How It Works

Streamlit powers the UI

TextBlob handles sentiment

RAKE + NLTK perform keyword extraction

SUMY (LexRank) generates summaries

PyPDF2 reads PDF text

deep-translator performs translation

Rule-based logic detects fake news

🧪 Technologies Used

Python 3

Streamlit

NLTK

TextBlob

RAKE-NLTK

SUMY

PyPDF2

deep-translator

📸 Screenshots (Add Later)
![Home UI](assets/screenshots/home.png)
![Summarizer](assets/screenshots/summary.png)
![Translation](assets/screenshots/translation.png)

📅 Future Enhancements

Add AI-powered chatbot (LLMs)

Add speech-to-text & text-to-speech

Add grammar correction tool

Add named entity recognition (NER)

Add dataset-based fake news ML model

Add export results as PDF

👨‍💻 Contributors
Name	Role
Aditya Prakash Gupta	Developer
Lakshya Gupta	Developer
❓ FAQ

Q: Does the app require GPU?
No, it runs on CPU.

Q: Does it work offline?
All tools except translation work offline.

Q: Is it beginner-friendly?
Yes — designed for learning and experimentation.

📜 License

This project is licensed under the MIT License.

🌟 Support

If you like this project, consider giving it a ⭐ on GitHub!
