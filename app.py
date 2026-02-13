import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("best_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Sentiment Analysis App")
st.write("Enter text to predict sentiment")

user_input = st.text_area("Text here:")

if st.button("Predict"):
    if user_input:
        vectorized_text = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_text)
        st.success(f"Predicted Sentiment: {prediction[0]}")
    else:
        st.warning("Please enter some text.")