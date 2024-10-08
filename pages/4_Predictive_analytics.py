import streamlit as st
import pandas as pd

# Set background color (Soft white lavender)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #fcfafc;  /* Soft white lavender background */
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

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

st.markdown("<h1 style='color: purple;'>Hospital Stay and ICU Admission Prediction</h1>", unsafe_allow_html=True)

# Section 1: Demographic and Lifestyle Information
st.markdown("<h2 style='color: purple;'>Demographic & Lifestyle</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30, key="age_input")
    gender = st.selectbox("Gender", ("Male", "Female"), key="gender_input")
    rural_urban = st.selectbox("Living Area", ("Urban", "Rural"), key="area_input")

with col2:
    smoking = st.selectbox("Smoking", ("Yes", "No"), key="smoking_input")
    alcohol = st.selectbox("Alcohol", ("Yes", "No"), key="alcohol_input")

# Section 2: Medical Conditions
st.markdown("<h2 style='color: purple;'>Medical Conditions</h2>", unsafe_allow_html=True)

# ECG selectboxes
previous_ecg = st.selectbox("Previous ECG?", ["No", "Yes"])

# Initialize selected_conditions_ecg as an empty list to avoid errors if not defined later
selected_conditions_ecg = []

# If 'Yes' is selected, show the second selectbox for Normal/Abnormal
if previous_ecg == "Yes":
    ecg_result = st.selectbox("Was the ECG Normal or Abnormal?", ["Normal", "Abnormal"])

    # If 'Abnormal' is selected, show the multiselect for specific conditions
    if ecg_result == "Abnormal":
        selected_conditions_ecg = st.multiselect(
            "Select the condition(s):",
            ["Pulmonary Embolism", 
             "Cardiogenic Shock", 
             "PSVT", 
             "Ventricular Tachycardia", 
             "Atrial Fibrillation", 
             "Sick Sinus Syndrome", 
             "Complete Heart Block", 
             "Heart Failure", 
             "STEMI", 
             "Acute Coronary Syndrome"]
        )

# Split layout into 2 columns
col3, col4 = st.columns(2)

# Column 1 selectboxes
with col3:
    # Anaemia selectbox
    selected_anaemia = st.selectbox("Anaemia:", ["No", "Anaemia", "Severe Anaemia"])
    
    # Heart Failure selectbox
    selected_heart_failure = st.selectbox(
        "Heart Failure:", 
        ["No", "Heart Failure", "Heart Failure with Reduced Ejection Fraction", "Heart Failure with Normal Ejection Fraction"]
    )

    # Shock selectbox
    selected_shock = st.selectbox("Shock:", ["No", "Shock", "Cardiogenic shock"])

# Column 2 selectboxes
with col4:
    # Infection selectbox
    infection_present = st.selectbox("Is there an infection?", ["No", "Yes"])

    # If "Yes" is selected, show the multiselect for specific infections
    if infection_present == "Yes":
        selected_infections = st.multiselect(
            "Select the type of infection:",
            ["Urinary Tract Infection", "Infective Endocarditis", "Chest Infection"]
        )
    
    # Cerebrovascular/Neuro condition selectbox
    cerebrovascular_condition = st.selectbox("Is there a Cerebrovascular/Neuro condition?", ["No", "Yes"])

    # If "Yes" is selected, show the multiselect for specific conditions
    if cerebrovascular_condition == "Yes":
        selected_conditions_neuro = st.multiselect(
            "Select the type of condition:",
            ["Cerebrovascular Accident Infarct", "Cerebrovascular Accident Bleed", "Neuro Cardiogenic Syncope"]
        )



col5, col6 = st.columns(2)

with col5:
    dm = st.selectbox("Diabetes Mellitus (DM)", ("Yes", "No"), key="dm_input")
    htn = st.selectbox("Hypertension (HTN)", ("Yes", "No"), key="htn_input")
    ckd = st.selectbox("Chronic Kidney Disease (CKD)", ("Yes", "No"), key="ckd_input")
    aki = st.selectbox("Acute Kidney Injury", ("Yes", "No"), key="aki_input")
    ortho = st.selectbox("Orthostatic", ("Yes", "No"), key="ortho_input")
    dvt = st.selectbox("Deep Venous Thrombosis", ("Yes", "No"), key="dvt_input")
    pemb = st.selectbox("Pulmonary Embolism", ("Yes", "No"), key="pemb_input")
    

with col6:
    ac_pain = st.selectbox("Atypical Chest Pain", ("Yes", "No"), key="acp_input")
    cardiac_enzymes = st.selectbox("Raised Cardiac Enzymes", ("Yes", "No"), key="enzymes_input")
    coronary_artery_disease = st.selectbox("Coronary Artery Disease", ("Yes", "No"), key="cad_input")
    prior_cardiomyopathy = st.selectbox("Prior Cardiomyopathy", ("Yes", "No"), key="cm_input")
    stable_angina = st.selectbox("Stable Angina", ("Yes", "No"), key="sa_input")
    valvular_heart_disease = st.selectbox("Valvular Heart Disease", ("Yes", "No"), key="vhd_input")
    congenital_heart_disease = st.selectbox("Congenital Heart Disease", ("Yes", "No"), key="chd_input")
    

    

# Section 3: Lab Values (Collapsible)
with st.expander("Enter Lab Values"):
    hb = st.number_input("Hemoglobin (HB)", min_value=6.4, max_value=18.3, value=13.0, key="hb_input")
    glucose = st.number_input("Glucose", min_value=1.2, max_value=294.0, value=90.0, key="glucose_input")
    leukocytes = st.number_input("Total Leucocytes Count", min_value=1.0, max_value=294.0, value=90.0, key="leukocyes_input")
    platelets = st.number_input("Platelets", min_value=1.0, max_value=294.0, value=90.0, key="platelets_input")
    urea = st.number_input("Urea", min_value=1.0, max_value=294.0, value=90.0, key="urea_input")
    crea = st.number_input("Creatinine", min_value=1.0, max_value=294.0, value=90.0, key="crea_input")



# Prediction Button
if st.button("Predict", key="predict_button"):
    # Collect inputs in a Pandas DataFrame, with condition values based on whether they are in selected_conditions_ecg
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Living Area': [rural_urban],
        'Smoking': [smoking],
        'Alcohol': [alcohol],
        'DM': [dm],
        'HTN': [htn],
        'Raised Cardiac Enzymes': [cardiac_enzymes],
        'HB': [hb],
        'Glucose': [glucose],
        'Pulmonary Embolism': ['Yes' if 'Pulmonary Embolism' in selected_conditions_ecg else 'No'],
        'Cardiogenic Shock': ['Yes' if 'Cardiogenic Shock' in selected_conditions_ecg else 'No'],
        'PSVT': ['Yes' if 'PSVT' in selected_conditions_ecg else 'No'],
        'Ventricular Tachycardia': ['Yes' if 'Ventricular Tachycardia' in selected_conditions_ecg else 'No'],
        'Atrial Fibrillation': ['Yes' if 'Atrial Fibrillation' in selected_conditions_ecg else 'No'],
        'Sick Sinus Syndrome': ['Yes' if 'Sick Sinus Syndrome' in selected_conditions_ecg else 'No'],
        'Complete Heart Block': ['Yes' if 'Complete Heart Block' in selected_conditions_ecg else 'No'],
        'Heart Failure': ['Yes' if 'Heart Failure' in selected_conditions_ecg else 'No'],
        'STEMI': ['Yes' if 'STEMI' in selected_conditions_ecg else 'No'],
        'Acute Coronary Syndrome': ['Yes' if 'Acute Coronary Syndrome' in selected_conditions_ecg else 'No']
    })

    input_data.rename_axis("Patient Entry")
    input_data.index = ["Patient Entry"]
                                         
                                         
    # Display the input data
    st.write("Collected Input Data:")
    st.write(input_data) 

    # Placeholder for prediction model (replace with actual model code)
    prediction_long_term = "Yes"  # Dummy result for long-term stay prediction
    prediction_icu = "No"  # Dummy result for ICU admission prediction

    # Display the predictions
    st.subheader("Prediction Results:")
    st.write(f"Long-term stay (7+ days): {prediction_long_term}")
    st.write(f"ICU admission: {prediction_icu}")
