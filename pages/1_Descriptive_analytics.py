import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dashboard_libraries import get_pvalue_propotion


st.set_page_config(
    page_title="PRAIS - Descriptive",
    page_icon="👋",
)

st.sidebar.image("./assets/P R A I S.png",)


df = pd.read_csv("data/HDHI_Admission_data_post_processed.csv")


st.header("Demographic information")



with st.container():
    if st.checkbox('Only ICU Admissions '):
        subset = df[df.ICU_admission_status == 1]
    else:
        subset = df

    # Group by 'Duration_Label' and 'GENDER' and count unique 'SNO'
    grouped_df = subset.groupby(['Duration_Label', 'GENDER']).agg({'SNO': pd.Series.nunique}).reset_index()

    # Rename the column to 'Unique_Encuonters_Count'
    grouped_df = grouped_df.rename(columns={'SNO': 'Unique_Encounters_Count'})

    # Calculate total unique SNO for each Duration_Label
    total_counts = subset.groupby('Duration_Label')['SNO'].nunique().reset_index().rename(
        columns={'SNO': 'Total_Unique_Encounters'})

    # Merge with grouped data
    merged_df = pd.merge(grouped_df, total_counts, on='Duration_Label')

    # Calculate proportion of each gender within every Duration_Label
    merged_df['Proportion'] = merged_df['Unique_Encounters_Count'] / merged_df['Total_Unique_Encounters']

    st.table(data=merged_df.sort_values(by="Duration_Label", ascending=False))

    # Group by 'Duration_Label' and 'GENDER' and count unique 'SNO'
    grouped_df = subset.groupby(['Duration_Label', 'RURAL']).agg({'SNO': pd.Series.nunique}).reset_index()

    # Rename the column to 'Unique_Encuonters_Count'
    grouped_df = grouped_df.rename(columns={'SNO': 'Unique_Encounters_Count'})

    # Calculate total unique SNO for each Duration_Label
    total_counts = subset.groupby('Duration_Label')['SNO'].nunique().reset_index().rename(
        columns={'SNO': 'Total_Unique_Encounters'})

    # Merge with grouped data
    merged_df = pd.merge(grouped_df, total_counts, on='Duration_Label')

    # Calculate proportion of each gender within every Duration_Label
    merged_df['Proportion'] = merged_df['Unique_Encounters_Count'] / merged_df['Total_Unique_Encounters']

    st.table(data=merged_df.sort_values(by="Duration_Label", ascending=False))

    subset.pivot(columns='Duration_Label', values="AGE").plot.hist(alpha=0.5, title="AGE", bins=50)

    # Show the plot in Streamlit
    st.pyplot(plt)


st.header("Laboratory results")

labs = ["Haemoglobin","TOTAL LEUKOCYTES COUNT","PLATELETS","GLUCOSE","UREA,CREATININE","B-TYPE NATRIURETIC PEPTIDE"]



option = st.selectbox(
    "Which laboratory results you want to review?",
    labs,
)

gender = st.selectbox(
    "What population do you want to include?",
    ["All", "Males", "Females"],
)

age_group  = st.selectbox(
    "What age group do you want to include?",
    ["All", "<18", "18 - 35", "36 - 65", ">65"],
)


if st.checkbox('Only ICU Admissions'):
    only_ICU = 1
else:
    only_ICU = 0


#Now using all of the parameters, create a subset of dataframe for visualization

# Case 1 - Keep whole dataset

if only_ICU == 1:
    subset1 = df[df.ICU_admission_status == 1]
else:
    subset1 = df

if gender == "Males":
    subset2 = subset1[subset1.boolGender == 1]
elif gender == "Females":
    subset2 = subset1[subset1.boolGender == 0]
else:
    subset2 = subset1


if age_group == "All":
    subset3 = subset2
else:
    subset3 = subset2[subset2.AgeGroup == age_group]

subset = subset3


number_encounters = subset.SNO.nunique()
total_number_encounters = df.SNO.nunique()
mean_value = subset[option].mean()
median_value = subset[option].median()

st.write("Number of encounters: {0:.0f}".format(number_encounters))
st.write("Percentage of all encounters in the dataset: {0:.2f}".format(100*number_encounters/total_number_encounters))
st.write("Mean value: {0:.2f}".format(mean_value))
st.write("Median value: {0:.2f}".format(median_value))



col1, col2 = st.columns(2)

with col1:

    subset.pivot(columns='Duration_Label', values=option).plot.hist(alpha=0.5, title=option, bins=50)

    # Show the plot in Streamlit
    st.pyplot(plt)


with col2:

    reference_values = pd.DataFrame(np.array([["<18", "X", "X"], ["18-35", "X", "X"], ["35-65", "X", "X"], ["65+", "X", "X"]]),
                 columns=['Age Group', 'Male', 'Female'])

    st.write("Reference value for: {}".format(option))
    st.table(data=reference_values)

st.header("Comorbidities")



with st.container():

    #conditions = ["boolGender", "boolRural", "SMOKING ","ALCOHOL","Diabetes Mellitus","Hypertension","Coronary Artery Disease","PRIOR CARDIOMYOPATHY","CHRONIC KIDNEY DISEASE"]


    conditions = ["boolGender", "boolRural", "SMOKING ","ALCOHOL","Diabetes Mellitus","Hypertension","Coronary Artery Disease",
                  "PRIOR CARDIOMYOPATHY","CHRONIC KIDNEY DISEASE",
   'SEVERE ANAEMIA', 'ANAEMIA', 'STABLE ANGINA',
       'Acute coronary Syndrome', 'ST ELEVATION MYOCARDIAL INFARCTION',
       'ATYPICAL CHEST PAIN', 'HEART FAILURE',
       'HEART FAILURE WITH REDUCED EJECTION FRACTION',
       'HEART FAILURE WITH NORMAL EJECTION FRACTION', 'Valvular Heart Disease',
       'Complete Heart Block', 'Sick sinus syndrome', 'ACUTE KIDNEY INJURY',
       'Cerebrovascular Accident INFRACT', 'Cerebrovascular Accident BLEED',
       'Atrial Fibrilation', 'Ventricular Tachycardia',
       'PAROXYSMAL SUPRA VENTRICULAR TACHYCARDIA', 'Congenital Heart Disease',
       'Urinary tract infection', 'NEURO CARDIOGENIC SYNCOPE', 'ORTHOSTATIC',
       'INFECTIVE ENDOCARDITIS', 'Deep venous thrombosis', 'CARDIOGENIC SHOCK',
       'SHOCK', 'PULMONARY EMBOLISM', 'CHEST INFECTION']

    option = st.selectbox(
        "Which comorbidity you want to review?",
        conditions,
    )

    #Charts don't make sense here, because it is hard to see trends
    #subset.pivot(columns='Duration_Label', values=option).plot.hist(alpha=0.5, title=option, bins=50)
    # Show the plot in Streamlit
    # st.pyplot(plt)

    if st.checkbox('Only ICU Admissions  '):
        only_ICU1 = 1
        subset = df[df.ICU_admission_status == 1]
    else:
        only_ICU1 = 0
        subset = df


    a = subset.groupby("Duration_Label")[option].sum().reset_index()
    b = subset.groupby("Duration_Label").SNO.count()
    x = pd.merge(a, b, on="Duration_Label")
    x["Perc"] = (x[option] / x['SNO']) * 100

    st.table(data=x.sort_values(by="Duration_Label", ascending=False))
    text, color = get_pvalue_propotion(subset, option, "Duration_Label")
    st.write(":{}[{}]".format(color, text))

    a = subset.groupby("ICU_admission_status")[option].sum().reset_index()
    b = subset.groupby("ICU_admission_status").SNO.count()
    x = pd.merge(a, b, on="ICU_admission_status")
    x["Perc"] = (x[option] / x['SNO']) * 100
    st.table(data=x)

    # If only ICU, then we can not calculate percentage, therefore only do this line below if NOT ICU
    if not only_ICU1:
        text, color = get_pvalue_propotion(subset, option, "ICU_admission_status")
        st.write(":{}[{}]".format(color, text))

