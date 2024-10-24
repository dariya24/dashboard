import streamlit as st


st.set_page_config(
    page_title="PRAIS - About",
    page_icon="❤",
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

# About page content
st.markdown("<h1 style='color: purple; margin-left: 0px; margin-top: 15px;'>About this Web Dashboard</h1>", unsafe_allow_html=True)

st.markdown("""
## Welcome to MediPredict
We are a group of health informatics students comprised of passionate data scientists and healthcare professionals working together to develop innovative solutions in medical prediction and analytics.

### Project description and objectives

For our PRAIS project, we are focusing on utilizing predictive analytics to provide insights into long-term hospital stays and ICU admissions. 

Our aim is that this would be of use for hospital managers and clinical coordinators within healthcare for optimizing care strategies and improving patient outcomes in future planning.

For the Descriptive tab, it provides key demographic and clinical data from the patient cohort, such as age distribution, prevalence of underlying conditions (e.g., diabetes, hypertension), and other general trends. These insights could be valuable for clinicians and healthcare administrators to understand patterns in the patient population, identify common risk factors, and assess the burden of disease across different demographics. For instance, new staff members or healthcare researchers might use this data to gain an overview of the typical patient population in their facility, helping them prepare for the kinds of challenges they are likely to face in practice.

The Diagnostic tab provides more targeted insights into specific diagnostic outcomes or indicators, such as the likelihood of patients requiring ICU admission based on specific clinical signs (e.g., elevated cardiac enzymes, abnormal ECG findings). This can be valuable for clinical decision-making, giving physicians and healthcare workers a quick overview of risk profiles based on available diagnostic data even though other factors would also play a role. It could also be of use in research, helping to identify areas where diagnostic protocols or guidelines could be refined based on observed patterns.

Clinicians could also use the Predictive tab as part of their daily work if integrated into the EHR.

### Design process
            
We wanted a simple, user-friendly design, with early stakeholder input throughout the process for every iteration. From card-based prototypes and user-testing to the finished product, from early adjustments to final refinements, we bring you our design. 

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
