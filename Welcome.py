import streamlit as st

# Set page config
st.set_page_config(
    page_title="Page 1 - PRAIS",
    page_icon="❤️",
)

# Inject CSS for sidebar links
custom_css = '''
/* Reset all possible styles on the sidebar links */
.st-emotion-cache-xtjyj5.eczjsme14 {
    color: #f0d7f2 !important;
    font-weight: bold !important;
    background-color: #f0d7f2 !important;
    text-shadow: none !important;
    box-shadow: none !important;
}

/* Target the active state specifically */
.st-emotion-cache-xtjyj5.eczjsme14.active {
    color: #f0d7f2 !important;
    font-weight: bold !important;
    background-color: #f0d7f2 !important;
    text-shadow: none !important;
    box-shadow: none !important;
}

/* Style for hovered link */
.st-emotion-cache-xtjyj5.eczjsme14:hover {
    background-color: #f0d7f2 !important;
    color: #f0d7f2 !important;
    font-weight: bold !important;
    border-radius: 5px; /* Optional: adds rounded corners */
}

/* Ensure the span within the link inherits these styles */
.st-emotion-cache-xtjyj5.eczjsme14.active .st-emotion-cache-1rtdyuf.eczjsme13 {
    color: #f0d7f2 !important;
    font-weight: bold !important;
}
'''

# Apply the CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Inject CSS to position the background image in the top-right corner
background_image_css = '''
<style>
/* Set the image in the top-right corner */
.top-right-image {
    position: absolute;
    top: 400px;
    right: 0px;
    width: 200px; /* Adjust the size of the image */
    height: auto;
    z-index: 1000; /* Ensure the image stays on top of other elements */
    padding: 10px; /* Add padding to create more space around the image */
}
</style>
'''

# Inject the CSS and HTML for the top-right image
st.markdown(background_image_css, unsafe_allow_html=True)

# Add the image in the top-right corner
st.markdown(
    '''
    <img src="https://img.goodfon.com/original/1920x1200/2/d1/badfon-taj-mahal-india-sunrise.jpg" class="top-right-image">
    ''',
    unsafe_allow_html=True
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
    top: 50px;
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
st.markdown("<h1 style='color: purple; margin-left: 0px; margin-top: -15px;'>PRAIS</h1>", unsafe_allow_html=True)
st.write("Welcome to MediPredict's Project PRAIS - Predicting Risk Admissions ICU Stays!")
st.write("**Why?** Identifying risk factors for, as well as predicting long-term hospital admission and ICU admission can improve future planning of resources. The PRAIS project aims to develop a predictive dashboard providing also descriptive and diagnostic data, using patient data from the Hero DMC Heart Institute, Ludhiana, Punjab, India.")
st.write("**For whom?** This work is crucial for hospital managers and clinical coordinators within healthcare to optimize care strategies and improve patient outcomes, particularly for patients at high risk of requiring extended hospital stays or ICU admissions.")

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.write("⬇️ Please scroll down for a virtual tour of the Hero DMC Heart Institute")

# Add space before the iframe
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# Embed the virtual tour iframe at the bottom of the page
st.markdown(
    '''
    <iframe src="https://herodmc.com/virtual-tour/dmc.html" width="90%" height="350" frameborder="0" allowfullscreen></iframe>
    ''',
    unsafe_allow_html=True
)
