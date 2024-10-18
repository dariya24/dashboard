import streamlit as st
import pandas as pd
from run_ML import get_ICU_ML_Prediction

st.set_page_config(
    page_title="PRAIS - About",
    page_icon="❤",
)
# Inject custom CSS to change the background color of the input fields to #f0d7f2
custom_css = '''
<style>
    /* Input fields such as number inputs and text inputs */
    input {
        background-color: #f0d7f2 !important;  /* Light purple background for input fields */
        border-radius: 5px !important;  /* Optional: Adds a slight border radius for a softer look */
        padding: 5px !important;  /* Optional: Adds padding inside the input fields */
    }

    /* Dropdown fields (select boxes) */
    select {
        background-color: #f0d7f2 !important;  /* Light purple background for select boxes */
        border-radius: 5px !important;  /* Optional: Adds a slight border radius for a softer look */
        padding: 5px !important;  /* Optional: Adds padding inside the select boxes */
    }
    
    /* Ensures number inputs are also styled correctly */
    [data-testid="stNumberInput"] > div > input {
        background-color: #f0d7f2 !important;
        border-radius: 5px !important;
        padding: 5px !important;
    }

    /* Ensures selectboxes are styled */
    [data-testid="stSelectbox"] > div > div {
        background-color: #f0d7f2 !important;
        border-radius: 5px !important;
    }

    /* Ensures multiselect boxes are styled */
    [data-testid="stMultiSelect"] > div > div {
        background-color: #f0d7f2 !important;
        border-radius: 5px !important;
    }
</style>
'''

# Inject the custom CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)


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

st.write("**Requirements**: To be able to predict hospital admissions you have to fill in all the fields below. There is no possibility to choose **Not applicable**. ")

# Section 1: Demographic and Lifestyle Information
st.markdown("<h2 style='color: black;'>Demographic & Lifestyle</h2>", unsafe_allow_html=True)
st.markdown("""
**Note**: The categories for **Smoking** and **Alcohol** are based on Yes/No answers. 
- For **Smoking**, 'Yes' includes current smokers or recent quitters.
- For **Alcohol**, 'Yes' refers to any alcohol consumption, but the dataset does not specify frequency or quantity.
""")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30, key="age_input")
    gender = st.selectbox("Gender", ("", "Male", "Female"), key="gender_input")  # Empty by default
    rural_urban = st.selectbox("Living Area", ("", "Urban", "Rural"), key="area_input")  # Empty by default

with col2:
    smoking = st.selectbox("Smoking", ("", "Yes", "No"), key="smoking_input")  # Empty by default
    alcohol = st.selectbox("Alcohol", ("", "Yes", "No"), key="alcohol_input")  # Empty by default

# Section 2: Medical Conditions
st.markdown("<h2 style='color: black;'>Medical Conditions</h2>", unsafe_allow_html=True)
# Place the st.write statement outside the column layout so it doesn't interfere with the columns
st.write("Every field will have the default **'No'** to save clicks if not relevant for the specific patient.")

# ECG selectboxes
previous_ecg = st.selectbox("Previous ECG?", ["No", "Yes"])  # No by default

# Initialize selected_conditions_ecg as an empty list to avoid errors if not defined later
selected_conditions_ecg = []

# If 'Yes' is selected, show the second selectbox for Normal/Abnormal
if previous_ecg == "Yes":
    ecg_result = st.selectbox("Was the ECG Normal or Abnormal?", ["Normal", "Abnormal"])

    # If 'Abnormal' is selected, show the multiselect for specific conditions
    if ecg_result == "Abnormal":
        selected_conditions_ecg = st.multiselect(
            "Select the condition(s):",
            ["Pulmonary Embolism (PE)",
             "Cardiogenic Shock",
             "Paroxysmal supraventricular tachycardia (PSVT)",
             "Ventricular Tachycardia (VT)",
             "Atrial Fibrillation (A-fib)",
             "Sick Sinus Syndrome (SSS)",
             "Complete Heart Block",
             "Heart Failure (HF)",
             "ST Elevation Myocardial Infarction (STEMI)",
             "Acute Coronary Syndrome (ACS)"]
        )

# Split layout into 2 columns
col3, col4 = st.columns(2)


# Column 1 selectboxes
with col3:
    # Anaemia selectbox
    selected_anaemia = st.selectbox("Anaemia:", ["No", "Anaemia", "Severe Anaemia"])  ## USED IN ICU ML

    # Heart Failure selectbox
    selected_heart_failure = st.selectbox(
        "Heart Failure:",
        ["No", "Heart Failure", "Heart Failure with Reduced Ejection Fraction",
         "Heart Failure with Normal Ejection Fraction"]
    )  # 'No' is the default selection

# Column 2 selectboxes can be added under col4 if needed
 

    # Shock selectbox
    selected_shock = st.selectbox("Shock:", ["No", "Shock", "Cardiogenic shock"])  # No by default

# Column 2 selectboxes
with col4:
    # Infection selectbox
    infection_present = st.selectbox("Is there an infection?", ["No", "Yes"])  # No by default

    # If "Yes" is selected, show the multiselect for specific infections
    if infection_present == "Yes":
        selected_infections = st.multiselect(
            "Select the type of infection:",
            ["Urinary Tract Infection (UTI)", "Infective Endocarditis", "Chest Infection"]
        )

    # Cerebrovascular/Neuro condition selectbox
    cerebrovascular_condition = st.selectbox("Is there a Cerebrovascular/Neuro condition?",
                                             ["No", "Yes"])  # No by default

    # If "Yes" is selected, show the multiselect for specific conditions
    if cerebrovascular_condition == "Yes":
        selected_conditions_neuro = st.multiselect(
            "Select the type of condition:",
            ["Cerebrovascular Accident Infarct", "Cerebrovascular Accident Bleed", "Neuro Cardiogenic Syncope"]
        )

# Additional Selectboxes (same treatment for defaults)
col5, col6 = st.columns(2)

with col5:
    dm = st.selectbox("Diabetes Mellitus (DM)", ("No", "Yes"), key="dm_input")
    htn = st.selectbox("Hypertension (HTN)", ("No", "Yes"), key="htn_input")
    ckd = st.selectbox("Chronic Kidney Disease (CKD)", ("No", "Yes"), key="ckd_input")  ## USED IN ICU ML
    aki = st.selectbox("Acute Kidney Injury", ("No", "Yes"), key="aki_input")  ## USED IN ICU ML
    ortho = st.selectbox("Orthostatic", ("No", "Yes"), key="ortho_input")
    dvt = st.selectbox("Deep Venous Thrombosis", ("No", "Yes"), key="dvt_input")
    pemb = st.selectbox("Pulmonary Embolism", ("No", "Yes"), key="pemb_input")

with col6:
    ac_pain = st.selectbox("Atypical Chest Pain", ("No", "Yes"), key="acp_input")
    cardiac_enzymes = st.selectbox("Raised Cardiac Enzymes", ("No", "Yes"), key="enzymes_input")  ## USED IN ICU ML
    coronary_artery_disease = st.selectbox("Coronary Artery Disease", ("No", "Yes"), key="cad_input")
    prior_cardiomyopathy = st.selectbox("Prior Cardiomyopathy", ("No", "Yes"), key="cm_input")  ## USED IN ICU ML
    stable_angina = st.selectbox("Stable Angina", ("No", "Yes"), key="sa_input")
    valvular_heart_disease = st.selectbox("Valvular Heart Disease", ("No", "Yes"), key="vhd_input")
    congenital_heart_disease = st.selectbox("Congenital Heart Disease", ("No", "Yes"), key="chd_input")


# Heading for the Lab Values section
st.markdown("<h2 style='color: black;'>Lab Values</h2>", unsafe_allow_html=True)
st.write("Lab units of measurement align with UCUM standards for interoperability and data exchange.")
st.write("Use the **+** or **-** buttons to adjust the values, or type directly in the box for quicker input. **Note:** Pressing too quickly on **+** or **-** might reload the page, but you won't lose any other information already entered.")
st.markdown("For unit conversions, you can use the [UCUM Web Tool](https://ucum.nlm.nih.gov/ucum-lhc/demo.html).")


# Section 3: Lab Values (Collapsible)
with st.expander("Enter Lab Values"):
    
    # Cached function to prevent unnecessary recalculations
    @st.cache_data
    def get_initial_lab_values():
        return {
            "hb": 13.0,
            "glucose": 90.0,
            "leukocytes": 7.5,
            "platelets": 250.0,
            "urea": 14.0,
            "crea": 1.0
        }

    # Retrieve initial values from cache
    lab_values = get_initial_lab_values()

    # Set up number inputs with step increments to avoid frequent reloading
    hb = st.number_input("Hemoglobin (HB) [g/dL]", min_value=3.0, max_value=26.5, value=lab_values['hb'], step=0.1, key="hb_input")
    glucose = st.number_input("Glucose [mg/dL]", min_value=1.2, max_value=888.0, value=lab_values['glucose'], step=1.0, key="glucose_input")
    leukocytes = st.number_input("Total Leukocytes Count [10^9/L]", min_value=0.1, max_value=261.0, value=lab_values['leukocytes'], step=0.1, key="leukocytes_input")
    platelets = st.number_input("Platelets [10^9/L]", min_value=0.58, max_value=1111.0, value=lab_values['platelets'], step=10.0, key="platelets_input")
    urea = st.number_input("Urea (BUN) [mg/dL]", min_value=0.1, max_value=495.0, value=lab_values['urea'], step=1.0, key="urea_input")
    crea = st.number_input("Creatinine [mg/dL]", min_value=0.065, max_value=15.63, value=lab_values['crea'], step=0.1, key="crea_input")




# Prediction Button
if st.button("Predict", key="predict_button"):
    # Collect inputs in a Pandas DataFrame, with condition values based on whether they are in selected_conditions_ecg
    input_data = pd.DataFrame({
        'Age': [age],  # -- used in ICU ML
        'Gender': [gender],
        'Living Area': [rural_urban],
        'Smoking': [smoking],
        'Alcohol': [alcohol],
        'DM': [dm],
        'HTN': [htn],
        'HB': [hb],  # -- used in ICU ML
        'Leukocytes': [leukocytes],  # -- used in ICU ML
        'Glucose': [glucose],  # -- used in ICU ML
        'Urea': [urea],  # -- used in ICU ML
        'Creatinine': [crea],  # -- used in ICU ML
        'Pulmonary Embolism': ['Yes' if 'Pulmonary Embolism' in selected_conditions_ecg else 'No'],

        'PSVT': ['Yes' if 'PSVT' in selected_conditions_ecg else 'No'],

        'Sick Sinus Syndrome': ['Yes' if 'Sick Sinus Syndrome' in selected_conditions_ecg else 'No'],

        # Please don't delete/change those rows, they are needed for ICU model
        'Prior_Cardiomyopathy': [prior_cardiomyopathy],
        'Chronic Kidney Disease': [ckd],
        'Raised Cardiac Enzymes': [cardiac_enzymes],
        'Anaemia': ['Yes' if 'Anaemia' in selected_anaemia else 'No'],
        'Stable Angina': [stable_angina],
        'Acute Coronary Syndrome': ['Yes' if 'Acute Coronary Syndrome' in selected_conditions_ecg else 'No'],
        'STEMI': ['Yes' if 'STEMI' in selected_conditions_ecg else 'No'],
        'Atypical Chest Pain': [ac_pain],
        'Heart Failure': ['Yes' if 'Heart Failure' in selected_conditions_ecg else 'No'],
        'Heart Failure with Reduced Ejection Fraction': [
            'Yes' if 'Heart Failure with Reduced Ejection Fraction' in selected_conditions_ecg else 'No'],
        'Heart Failure with Normal Ejection Fraction': [
            'Yes' if 'Heart Failure with Normal Ejection Fraction' in selected_conditions_ecg else 'No'],
        'Complete Heart Block': ['Yes' if 'Complete Heart Block' in selected_conditions_ecg else 'No'],
        'Acute Kidney Injury': [aki],
        'Atrial Fibrillation': ['Yes' if 'Atrial Fibrillation' in selected_conditions_ecg else 'No'],
        'Ventricular Tachycardia': ['Yes' if 'Ventricular Tachycardia' in selected_conditions_ecg else 'No'],
        'Cardiogenic Shock': ['Yes' if 'Cardiogenic Shock' in selected_conditions_ecg else 'No'],
        'Shock': ['Yes' if 'Shock' in selected_conditions_ecg else 'No'],

    })

    input_data.rename_axis("Patient Entry")
    input_data.index = ["Patient Entry"]

    # Display the input data
    st.write("Collected Input Data:")
    st.write(input_data)

    prediction_result, data = get_ICU_ML_Prediction(input_data)

    st.write("Collected Input Data for ML")
    st.write(data)

    if prediction_result == 1:
        prediction_icu = "Yes"
    else:
        prediction_icu = "No"

    # Placeholder for prediction model (replace with actual model code)
    prediction_long_term = "Yes"  # Dummy result for long-term stay prediction

    # Display the predictions
    st.subheader("Prediction Results:")
    st.write(f"Long-term stay (7+ days): {prediction_long_term}")
    st.write(f"ICU admission: {prediction_icu}")

