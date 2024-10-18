import streamlit as st

st.set_page_config(
    page_title="PRAIS - About",
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

For our PRAIS project, we are focusing on utilizing predictive analytics to provide insights into long-term hospital stays and ICU admissions that might be of use for hospital managers and clinical coordinators within healthcare for optimizing care strategies and improving patient outcomes.

**References**  
<a href="https://www.herodmc.com/" target="_blank">Hero DMC Heart Institute Website</a>  

<a href="https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data?select=HDHI+Admission+data.csv" target="_blank">Dataset - Hospital Admissions Data on Kaggle</a>  
""", unsafe_allow_html=True)

# Add info button for extra details about the dataset
with st.expander("ℹ️ More information about the dataset"):
    st.write("""
    The data used in this study was collected from patients admitted to the Hero DMC Heart Institute, Ludhiana, Punjab, India, 
    between April 1, 2017, and March 31, 2019. Over this two-year period, 14,845 admissions were recorded, corresponding 
    to 12,238 unique patients, including 1,921 patients with multiple admissions. The hospital is a tertiary care facility 
    affiliated with Dayanand Medical College and Hospital.

    The dataset includes patient demographics (age, sex, and locality), admission details (emergency or outpatient), medical history 
    (smoking, alcohol use, diabetes, hypertension, coronary artery disease, cardiomyopathy, chronic kidney disease), and laboratory 
    results (hemoglobin, total lymphocyte count, platelets, glucose, urea, creatinine, brain natriuretic peptide, raised cardiac enzymes, and ejection fraction).

    In total, 28 features related to comorbidities, including heart failure, STEMI, pulmonary embolism, and types of shock, were recorded. 
    Shock was classified into categories such as non-cardiac and cardiogenic shock, with some cases considered multifactorial.

    For analysis, we retained 17 key features, including prior cardiomyopathy, chronic kidney disease, raised cardiac enzymes, various heart failure 
    types, and conditions such as atrial fibrillation, ventricular tachycardia, and cardiogenic shock. Laboratory values were also maintained as part of the final dataset.
    """)

# Team Members
st.markdown("""
### Team Members:
""")

# Paths to the images
image_paths = [
    "assets/Dariia.jpg",
    "assets/Martin.jpg",
    "assets/Sandra.jpg",
    "assets/Roosa.jpg",
    "assets/Umiah.jpg",
    "assets/Anna.jpg"
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
st.image("assets/PRAIS.png", use_column_width=False, width=500)
