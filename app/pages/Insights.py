import streamlit as st 
from utils.styles import apply_theme
apply_theme()

import pandas as pd
import plotly.express as px 

st.title("Dataset Insights")
st.write("Exploring the IMDB 50k Reviews dataset")

df=pd.read_csv("data/sample_reviews.csv")

tab1,tab2,tab3= st.tabs(["Overview", "Review Length Analysis","Word Clouds"])
with tab1:
    fig= px.pie(df, names='sentiment',color_discrete_map={'positive': '#2ecc71', 'negative': '#e74c3c'},
                title='Positive vs Negative Reviews')
    st.plotly_chart(fig)
    col1,col2= st.columns(2)
    with col1:
        st.metric("Total Reviews", "50,000")
        st.metric("Positive Reviews", "25,000")
    with col2:
        st.metric("Negative Reviews", "25,000")
        st.metric("Vocabulary Size", "~50,000")

with tab2:
    df['word_count']=df['review'].apply(lambda x: len(str(x).split()))
    fig= px.histogram(df, x='word_count',color='sentiment',barmode='overlay',
                      color_discrete_map={'positive': '#2ecc71', 'negative': '#e74c3c'},
                      title='Word Count by Sentiment')
    st.plotly_chart(fig)

    st.subheader("Review Length Distribution")
    st.image('assets/length_distribution.png')
    st.markdown("""
    Most reviews fall between 100-400 words.
    The distribution is right-skewed,
    a few users write very long reviews.
    """)

with tab3:
    col1,col2= st.columns(2)
    with col1:
        st.markdown("Positve Reviews")
        st.image("assets/wordcloud_positive.png")
    with col2:
        st.markdown("Negative Reviews")
        st.image("assets/wordcloud_negative.png")