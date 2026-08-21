import streamlit as st
import nltk

st.set_page_config(
    page_title="SentimentScope",
    page_icon=":movie_camera:",
    layout="wide"
)

@st.cache_resource
def download_nltk_data():
    nltk.download("stopwords", quiet=True)
    nltk.download("wordnet", quiet=True)
    nltk.download("punkt", quiet=True)
download_nltk_data()

st.markdown("""
<style>

/* Remove default Streamlit top padding */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 2rem !important;
}

/* Remove header space */
header[data-testid="stHeader"] {
    background: transparent;
    height: 0;
}

div[data-testid="stToolbar"] {
    display: none;
}

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0F1923 0%,
        #1A2634 50%,
        #0F1923 100%
    );
}

/* All headings */
h1, h2, h3 {
    color: #E8E8E8 !important;
    font-weight: 700 !important;
}

/* Body text */
p, li {
    color: #B0BEC5 !important;
    font-size: 1rem !important;
    line-height: 1.7 !important;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(229,9,20,0.3);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
}

div[data-testid="metric-container"]:hover {
    border-color: #E50914;
    transform: translateY(-3px);
    transition: all 0.2s;
}

div[data-testid="metric-container"] label {
    color: #E50914 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

div[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(10,18,26,0.98) !important;
    border-right: 1px solid rgba(229,9,20,0.2);
}

/* Divider */
hr {
    border-color: rgba(229,9,20,0.25) !important;
    margin: 1.5rem 0 !important;
}

/* Buttons */
.stButton button {
    background: #E50914 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

.stButton button:hover {
    background: #FF1A1A !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 15px rgba(229,9,20,0.4) !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align: center;
    padding: 60px 20px 40px 20px;
    background: linear-gradient(
        180deg,
        rgba(229,9,20,0.08) 0%,
        transparent 100%
    );
    margin-bottom: 10px;
">
    <h1 style="
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 12px;
        color: white !important;
    ">
        SentimentScope
    </h1>
    <p style="
        color: #B0BEC5;
        font-size: 1.15rem;
        max-width: 500px;
        margin: auto;
    ">
        AI-Powered Movie Review Sentiment Analyser
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

#Description columns 
col1, col2 = st.columns(2)

with col1:
    st.markdown("### What does this app do?")
    st.markdown("""
    SentimentScope analyses the sentiment of movie 
    reviews using Natural Language Processing, 
    instantly telling you whether a review is 
    **positive** or **negative** and how confident 
    the model is.
    """)

with col2:
    st.markdown("### How to use it:")
    st.markdown("""
    1. **Analyse Review** : paste any movie review
    2. **Data Insights** : explore IMDB dataset patterns
    3. **Model Info** : understand the NLP pipeline
    """)

st.divider()

#Metrics
st.markdown("### Model Performance")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Training Reviews", "40,000")
col2.metric("Test Reviews", "10,000")
col3.metric("Accuracy", "90.8%")
col4.metric("ROC-AUC", "0.96")

st.divider()

#Call to action
st.markdown("""
<div style="
    text-align: center;
    padding: 24px;
    background: rgba(229,9,20,0.08);
    border-radius: 12px;
    border: 1px solid rgba(229,9,20,0.2)
">
    <p style="color:#E8E8E8; font-size:1.1rem; margin:0 0 8px 0">
        Use the sidebar to navigate between pages
    </p>
    <p style="color:#B0BEC5; margin:0">
        Start with <strong>Analyse Review</strong> 
        to try the app instantly
    </p>
</div>
""", unsafe_allow_html=True)