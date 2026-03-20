🧠 AI Legislative Analyzer

An intelligent system that analyzes legal documents, bills, and policies using AI to simplify complex legal language and provide meaningful insights.

📌 Project Overview

The AI Legislative Analyzer is designed to help users understand legal documents easily. It uses Natural Language Processing (NLP) and Machine Learning (ML) techniques to:

Analyze legal text

Extract key insights

Detect risks or ambiguities

Summarize complex laws into simple language

This project aims to make legal information accessible to everyone, even without a legal background.

🚀 Features

📄 Upload and analyze legal documents

🧾 Automatic summarization of laws

⚠️ Risk & ambiguity detection

🔍 Keyword and clause extraction

🤖 AI-based interpretation of legal text

📊 Clean and user-friendly dashboard

🛠️ Tech Stack

Frontend:

HTML

CSS

JavaScript

Backend:

Python (Flask)

Machine Learning:

NLP (Natural Language Processing)

Scikit-learn / Transformers

Database:

MySQL / MongoDB

▶️ How to Run the Project


🔹 Step 1: Install Requirements

Make sure Python is installed (Python 3.8+ recommended)

pip install -r requirements.txt
🔹 Step 2: Run Backend Server

Go to backend folder (if separated):

cd backend
python app.py

👉 You should see:

Running on http://127.0.0.1:5000/
🔹 Step 3: Run Frontend
Option 1 (Simple):

Open index.html in browser

Option 2 (Recommended):

Use Live Server (VS Code)

🔹 Step 5: Connect Frontend with Backend

Ensure API calls point to:

http://127.0.0.1:5000/analyze

Example:

fetch("http://127.0.0.1:5000/analyze", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: inputText })
})


⚙️ How It Works

User uploads or inputs a legal document

Text is preprocessed (cleaning, tokenization)

NLP models analyze the content

System generates:

Summary

Risk indicators

Key insights

Results are displayed on the dashboard

🔗 Connecting Frontend & Backend

Ensure Flask server is running (localhost:5000)

Use API endpoints in JavaScript (fetch or axios)

Example:

fetch("http://127.0.0.1:5000/analyze", {
  method: "POST",
  body: JSON.stringify({ text: inputText }),
  headers: { "Content-Type": "application/json" }
})

Future Enhancements

🌐 Multi-language support

📱 Mobile app integration

🔊 Voice-based explanation

📊 Advanced analytics dashboard

⭐ Conclusion

The AI Legislative Analyzer simplifies complex legal content using AI, making laws more transparent and understandable for everyone.