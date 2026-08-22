import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
    }

    header[data-testid="stHeader"] {
        background: transparent;
        height: 0;
    }

    div[data-testid="stToolbar"] {
        display: none;
    }

    .stApp {
        background: linear-gradient(
            135deg,
            #0F1923 0%,
            #1A2634 50%,
            #0F1923 100%
        );
    }

    h1, h2, h3 {
        color: #E8E8E8 !important;
        font-weight: 700 !important;
    }

    p, li {
        color: #B0BEC5 !important;
        font-size: 1rem !important;
        line-height: 1.7 !important;
    }

    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(229,9,20,0.3);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }

    div[data-testid="metric-container"]:hover {
        border-color: #8B1A1A;
        transform: translateY(-3px);
        transition: all 0.2s;
    }

    div[data-testid="metric-container"] label {
        color: #8B1A1A !important;
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

    section[data-testid="stSidebar"] {
        background: rgba(10,18,26,0.98) !important;
        border-right: 1px solid rgba(229,9,20,0.2);
    }

    hr {
        border-color: rgba(229,9,20,0.25) !important;
        margin: 1.5rem 0 !important;
    }

    .stButton button {
        background: #8B1A1A !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    .stButton button:hover {
        background: #A52020 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px 
            rgba(229,9,20,0.4) !important;
    }

    </style>
    """, unsafe_allow_html=True)