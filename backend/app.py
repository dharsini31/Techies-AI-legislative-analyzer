from flask import Flask, request, jsonify
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def extract_text(pdf):
    text = ""
    with pdfplumber.open(pdf) as pdf_file:
        for page in pdf_file.pages:
            text += page.extract_text() or ""
    return text

def summarize_text(text, num_sentences=5):
    sentences = text.split('.')

    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)

    scores = np.array(X.sum(axis=1)).flatten()

    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)),
        reverse=True
    )

    top_sentences = [s for _, s in ranked_sentences[:num_sentences]]
    return ". ".join(top_sentences)

def compress_text(text):
    sentences = text.split('.')

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)

    scores = np.array(X.sum(axis=1)).flatten()

    ranked = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)),
        reverse=True
    )

    top_sentences = [s for _, s in ranked[:50]]
    return " ".join(top_sentences)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    text = extract_text(file)

    original_tokens = len(text.split())

    compressed = compress_text(text)
    compressed_tokens = len(compressed.split())

    summary = summarize_text(compressed, num_sentences=7)

    return jsonify({
        "summary": summary,
        "original_tokens": original_tokens,
        "compressed_tokens": compressed_tokens,
        "reduction_percent": round(
            ((original_tokens - compressed_tokens)/original_tokens)*100, 2
        )
    })

if __name__ == '__main__':
    app.run(debug=True)