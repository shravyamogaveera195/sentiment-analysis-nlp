import streamlit as st 
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#import matplotlib.pyplot as plt

#loading models
tfidf= joblib.load(r"C:\Users\shreyaash mogaveera\sentiment-analysis-nlp\model\tfidf_vectorizer.pkl")
lr_model= joblib.load(r"C:\Users\shreyaash mogaveera\sentiment-analysis-nlp\model\lr_model.pkl")
svc_model= joblib.load(r"C:\Users\shreyaash mogaveera\sentiment-analysis-nlp\model\svc_model.pkl")

def preprocess(text):
    text=re.sub(r'<.*?>','',text)
    text=re.sub(r'http\S+|www\S+','',text)
    text=re.sub(r'[^a-zA-Z\s]','',text)
    text=text.lower().strip()
    text=re.sub(r'\s+',' ',text)
    stop_words=set(stopwords.words('english'))
    negation_words={'not','no','nor','neither','never',"don't","doesn't","didn't"}
    stop_words=stop_words-negation_words
    lemmatizer=WordNetLemmatizer()
    tokens= [lemmatizer.lemmatize(t) for t in text.split() if t not in stop_words]
    return ' '.join(tokens)

st.title("Analyse a Movie Review")

#Example for quick testing
col1, col2= st.columns(2)
with col1:
    if st.button("Positive Example"):
        st.session_state['review']=(
            "This film is an absolute masterpiece and amazing. The performances"
            " are outstanding and the story kept me engaged throughout"
        )

with col2:
    if st.button("Negative Example"):
            st.session_state['review']=(
                "Terrible waste of time. The plot makes no sense and "
                "the acting is worse. Avoid at all costs"
            )

review_input=st.text_area(
     "Paste your movie review heare:",
     value=st.session_state.get('review', ''),
     height=150
)

model_choice= st.radio(
     "Choose model:",
     ["Linear_SVC","Logistic_Regression"],horizontal=True
)

if st.button("Analyse Sentiment", type="primary",use_container_width=True):
    if not review_input.strip():
        st.warning("Please enter a review first!!")
    else:
        with st.spinner("Analysing..."):
             processed=preprocess(review_input)
             vectorized=tfidf.transform([processed])
             

             if model_choice=="Linear_SVC":
                 model= svc_model
                 decision_score= model.decision_function(vectorized)[0]
                 import numpy as np
                 confidence= 1/(1+ np.exp(-abs(decision_score))) 
             else:
                  model=lr_model
                  if vectorized.shape[1] > 50000:
                     vectorized = vectorized[:, :50000]
                  probabilty= model.predict_proba(vectorized)[0]
                  confidence= max(probabilty)

        prediction = model.predict(vectorized)[0]
        sentiment= "POSITIVE" if prediction==1 else "NEGATIVE"

        if prediction==1:
            st.success(f"POSITIVE SENTIMENT")
        else:
            st.error(f"NEGATIVE SENTIMENT")

        col1,col2,col3 = st.columns(3)
        col1.metric("Sentiment", sentiment)
        col2.metric("Confidence", f"{confidence:.2%}")
        col3.metric("Model",model_choice.split()[0])

        