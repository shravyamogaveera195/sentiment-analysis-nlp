import streamlit as st 
from utils.styles import apply_theme
apply_theme()

st.title("How it Works")

tab1,tab2,tab3= st.tabs(["NLP Pipeline", "Model Performance", "Model Comparision"])

with tab1:
    st.subheader("Text Processing Pipeline")
    st.markdown("""
    **Step 1 - Text Cleaning**
    Remove HTML tags, special characters, lowercase
    
    **Step 2 - Tokenization**
    Split text into individual words

    **Step 3 - Stopword Removal**
    Remove common words BUT keep negation words
    "not good" stays as "not good"

    **Step 4 - Lemmatization**
    "running" to "run", "better" to "good"

    **Step 5 - TF-IDF Vectorization**
    Convert text to numbers
    Uses bigrams: "not good" = one feature

    **Step 6 - Prediction**
    Linear SVC predicts probability
    """)

with tab2:
    col1,col2= st.columns(2)
    with col1:
        st.metric("Accuracy","90.9%")
        st.metric("ROC-AUC", "0.96")
    with col2:
        st.metric("Precision","90.5%")
        st.metric("Recall","91.4%")
    st.image("assets/confusion_matrix.png")
    st.image("assets/roc_curve.png")

with tab3:
    st.image("assets/model_comparision.png")
    st.markdown(""" 
    | Model | Accuracy |
    |---|---|
    | Logistic Regression | 90.4% |
    | Naive Bayes Complement | 88.3% |
    | Naive Bayes Multinomial | 88.3% |
    | Linear SVC | 90.9% |
    """)