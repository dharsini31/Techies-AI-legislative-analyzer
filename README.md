# ⚖️ AI Legislative Analyzer  
### Pipeline Optimization for Large-Scale Legal Document Analysis

---

## 📌 Overview

The **AI Legislative Analyzer** is a pipeline-optimized system designed to simplify and analyze complex legal and government documents. It processes large policy documents efficiently by reducing unnecessary content and generating concise, meaningful summaries.

This project focuses on **Pipeline Optimization**, ensuring faster processing, reduced computational cost, and scalable performance.

---

## 🚀 Problem Statement

Legal and government documents are often:
- Extremely long (100k+ tokens)
- Difficult to understand for common users
- Expensive to process using AI models

Our solution optimizes the processing pipeline to make legal information:
- ✅ Faster to analyze  
- ✅ Cost-efficient  
- ✅ Easy to understand  

---

## 💡 Solution Approach

We designed a **multi-stage optimized pipeline**:

1. **Text Extraction**
   - Extract text from PDF using `pdfPlumber`

2. **Preprocessing**
   - Clean and normalize text
   - Remove noise and stopwords

3. **Chunking**
   - Split large documents into smaller parts

4. **Relevance Filtering (TF-IDF)**
   - Rank and select important content
   - Remove low-value text

5. **Token Compression**
   - Reduce input size before summarization

6. **Summarization**
   - Generate concise summaries

7. **Output Dashboard**
   - Display simplified results and metrics

---

## ⚙️ Pipeline Optimization Techniques

- 🔹 Parallel processing of text chunks  
- 🔹 Token reduction using TF-IDF filtering  
- 🔹 Early-stage filtering to avoid unnecessary computation  
- 🔹 Efficient data flow between pipeline stages  

---

## 📊 Measurable Results

| Metric                     | Value              |
|--------------------------|-------------------|
| Original Tokens          | 120,000           |
| Tokens After Compression | 28,000            |
| Token Reduction          | ~76%              |
| Cost Reduction           | ~70%              |
| Processing Time Improved | ~40% faster       |

---

## 🌍 Real-World Applications

- Government policy simplification  
- Legal document analysis  
- Educational tools for law students  
- Public awareness platforms  
- NGO and research use  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, FastAPI  
- **Libraries:**  
  - pdfPlumber  
  - NLTK  
  - Scikit-learn (TF-IDF)  

---
