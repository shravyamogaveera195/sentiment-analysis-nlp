import streamlit as st
import nltk

st.set_page_config(page_title="SentimentScope", page_icon=":movie_camera:",layout="wide")

@st.cache_resource
def download_nltk_data():
    nltk.download("stopwords",quiet=True)
    nltk.download("wordnet",quiet=True)
    nltk.download("punkt",quiet=True)
download_nltk_data()

st.title("SentimentScope")
st.subheader("AI-Poweres Movie review sentiment analyser")

st.markdown("""
### What does this app do?
SentimentScope analyses the sentiment of movie reviews using Natural Language Processsing.

### How to use it:
1. Analyse Review - paste any movie review
2. Data Insights - explore patterns in IMDB dataset
3. Model Info - understand how the NLP pipeline works
""")

col1,col2,col3,col4 = st.columns(4)
col1.metric("Training Reviews", "40,000")
col2.metric("Test Reviews", "10,000")
col3.metric("Accuracy", "90.8%")
col4.metric("ROC-AUC", "0.96")