import streamlit as st
import pandas as pd
import numpy as np

#this sets page title and icon, non critical
st.set_page_config(
    page_title="Page 1 - PRAIS",
    page_icon="❤️",
)

# Sidebar background with reduced opacity for image only
sidebar_bg = '''
<style>
[data-testid="stSidebar"] {
    position: relative;
    background: none;  /* Remove any default background */
}

[data-testid="stSidebar"]::before {
    content: "";
    background-image: url("https://clipart-library.com/images_k/anatomical-heart-silhouette/anatomical-heart-silhouette-19.png");
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    opacity: 0.6;  /* Apply opacity only to background image */
    z-index: -1;  /* Keep image behind the text */
}

/* Set darker text color in the sidebar */
[data-testid="stSidebar"] .css-1d391kg p, [data-testid="stSidebar"] .css-1d391kg {
    color: black;  /* Dark text */
}
</style>
'''

st.markdown(sidebar_bg, unsafe_allow_html=True)

# Main content here
st.markdown("<h1 style='color: red;'>PRAIS</h1>", unsafe_allow_html=True)
st.write("Welcome to MediPredict's Project for helping you help patient's with Heart Disease")
st.write("The Identifying Risk Factors and Predicting Long Term Hospital Admission and ICU Admission (PRAIS) project aims to develop a predictive dashboard using patient data from the Hero DMC Heart Institute, Ludhiana, Punjab, India. The project’s main goal is to analyze risk factors and create predictive models that help clinicians and hospital staff optimize resource management and improve patient outcomes by predicting long-term hospital stays and ICU admissions.  ")

