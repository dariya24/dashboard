import streamlit as st

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


# About page content
st.title("About MediPredict")

st.markdown("""
## Welcome to MediPredict
We are a group of health informatics student comprised of passionate data scientists and healthcare professionals working together to develop innovative solutions in medical prediction and analytics.

For our PRAIS project we are focusing on utilizing predictive analytics to provide insights into long-term hospital stays and ICU admissions.

### Team Members:
- **Ching Hong So**
- **Dariia Reshetukha**
- **Sandra Johansson**
- **Roosa Hyppölä**
- **Umiah Gohar**
- **Anna Axell**
            
References

For any inquiries, please contact us via our collective email:
📧 **medipredict@stud.dsv.su.se**
""")

# Optional: Logo

st.image("C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Dashboard/Streamlit session Test/PRAIS.png", use_column_width=False, width=400)