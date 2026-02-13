# 💬 Sentiment Analysis App

A Machine Learning web application that predicts whether a given text expresses positive or negative sentiment.

---

## 🚀 Live Demo

https://sentiment-analysis-app-6hxrmm5kdsa9ngmxozh8ek.streamlit.app/

---

## 📊 Project Overview

This project uses classical Machine Learning models to perform sentiment classification on text data.

The best-performing model is selected based on accuracy and deployed using Streamlit.

---

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- TF-IDF Vectorization  
- Streamlit  
- Pandas  
- NumPy  
- Joblib  

---

## 🧠 Models Tested

- Logistic Regression  
- Naive Bayes  
- Linear SVM  
- Random Forest  

The best model was selected based on accuracy.

---

## 📂 Project Structure

sentiment-analysis-app/
│
├── app.py                     # Streamlit web application
├── Analysis.ipynb             # Model training & experimentation
├── best_sentiment_model.pkl   # Saved trained model
├── tfidf_vectorizer.pkl       # Saved TF-IDF vectorizer
├── requirements.txt           # Dependencies
└── dataset files              # Training dataset

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/shanmukjavvadi/sentiment-analysis-app.git
cd sentiment-analysis-app
pip install -r requirements.txt
streamlit run app.py

---

# 🚀 Optional But Powerful Upgrade

Add this section at the bottom:

```markdown
---

## 🎯 Key Highlights

- Compared multiple ML classification models
- Implemented TF-IDF feature extraction
- Selected best-performing model based on evaluation metrics
- Serialized trained model using Joblib
- Deployed a live web application using Streamlit Cloud
