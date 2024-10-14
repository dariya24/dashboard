import streamlit as st

st.set_page_config(
    page_title="PRAIS - Descriptive",
    page_icon="❤",
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

# About page content
st.markdown("<h1 style='color: purple;'>About MediPredict</h1>", unsafe_allow_html=True)

st.markdown("""
## Welcome to MediPredict
We are a group of health informatics students comprised of passionate data scientists and healthcare professionals working together to develop innovative solutions in medical prediction and analytics.

For our PRAIS project, we are focusing on utilizing predictive analytics to provide insights into long-term hospital stays and ICU admissions.

### Team Members:
""")

# Paths to the images
image_paths = [
    "C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Exercise/dashboard/assets/Dariia.jpg",
    "C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Exercise/dashboard/assets/Martin.jpg",
    "C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Exercise/dashboard/assets/Sandra.jpg",
    "C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Exercise/dashboard/assets/Roosa.jpg",
    "C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Exercise/dashboard/assets/Umiah.jpg",
    "C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Exercise/dashboard/assets/Anna.jpg"
]

# Corresponding names and titles
people_info = [
    ("Dariia Reshetukha", "Technical lead"),
    ("Ching Hong So", "Data and Machine Learning Specialist"),
    ("Sandra Johansson", "Documentation Lead"),
    ("Roosa Hyppölä", "Quality Assurance Lead"),
    ("Umiah Gohar", "Stakeholder Contact Person"),
    ("Anna Axell", "Clinical Advisor")
]

# Display images and info in two rows, 3 columns per row
for row in range(0, len(image_paths), 3):
    cols = st.columns(3)
    for i, col in enumerate(cols):
        if row + i < len(image_paths):
            with col:
                st.image(image_paths[row + i], width=150)  # Adjust the width for smaller pictures
                st.write(f"**{people_info[row + i][0]}**")  # Name
                st.write(people_info[row + i][1])  # Title

# References
st.markdown("""
For any inquiries, please contact us via our collective email:
📧 **medipredict@stud.dsv.su.se**
""")

# Optional: Logo
st.image("C:/Users/PC/OneDrive/Dokument/Master i Hälsoinformatik/SU/HT24/Dashboard/Streamlit session Test/PRAIS.png", use_column_width=False, width=400)
