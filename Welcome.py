import streamlit as st

# Set page config
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
st.markdown("<h1 style='color: purple;'>PRAIS</h1>", unsafe_allow_html=True)
st.write("Welcome to MediPredict's Project PRAIS - Predicting Risk Admissions ICU Stays!")
st.write("**Why?** Identifying risk factors for, as well as predicting long-term hospital admission and ICU admission can improve future planning of resources. The PRAIS project aims to develop a predictive dashboard providing also descriptive and diagnostic data, using patient data from the Hero DMC Heart Institute, Ludhiana, Punjab, India.")
st.write("**For whom?** This work is crucial for hospital managers and clinical coordinators within healthcare to optimize care strategies and improve patient outcomes, particularly for patients at high risk of requiring extended hospital stays or ICU admissions.")

# Add space before the iframe
st.markdown("<br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.write("**Join a virtual tour at the Hero DMC Heart Institute.**")

# Embed the virtual tour iframe at the bottom of the page
st.markdown(
    '''
    <iframe src="https://herodmc.com/virtual-tour/dmc.html" width="90%" height="350" frameborder="0" allowfullscreen></iframe>
    ''',
    unsafe_allow_html=True
)
