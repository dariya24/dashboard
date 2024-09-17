import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

    a = subset.groupby("Duration_Label")["boolGender"].sum().reset_index()
    b = subset.groupby("Duration_Label").SNO.count()
    x = pd.merge(a, b, on="Duration_Label")
    x["Perc"] = (x["boolGender"] / x['SNO']) * 100

    st.table(data=x)

    a = subset.groupby("Duration_Label")["boolRural"].sum().reset_index()
    b = subset.groupby("Duration_Label").SNO.count()
    x = pd.merge(a, b, on="Duration_Label")
    x["Perc"] = (x["boolRural"] / x['SNO']) * 100

    st.table(data=x)

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

st.write("Number of encounters: {}".format(number_encounters))
st.write("Percentage of all encounters in the dataset: {}".format(number_encounters/total_number_encounters))
st.write("Mean value: {}".format(mean_value))
st.write("Median value: {}".format(median_value))



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

    conditions = ["SMOKING ","ALCOHOL","Diabetes Mellitus","Hypertension","Coronary Artery Disease","PRIOR CARDIOMYOPATHY","CHRONIC KIDNEY DISEASE"]

    option = st.selectbox(
        "Which comorbidity you want to review?",
        conditions,
    )

    #Charts don't make sense here, because it is hard to see trends
    #subset.pivot(columns='Duration_Label', values=option).plot.hist(alpha=0.5, title=option, bins=50)
    # Show the plot in Streamlit
    # st.pyplot(plt)

    if st.checkbox('Only ICU Admissions  '):
        subset = df[df.ICU_admission_status == 1]
    else:
        subset = df

    a = subset.groupby("Duration_Label")[option].sum().reset_index()
    b = subset.groupby("Duration_Label").SNO.count()
    x = pd.merge(a, b, on="Duration_Label")
    x["Perc"] = (x[option] / x['SNO']) * 100

    st.table(data=x)

    a = subset.groupby("ICU_admission_status")[option].sum().reset_index()
    b = subset.groupby("ICU_admission_status").SNO.count()
    x = pd.merge(a, b, on="ICU_admission_status")
    x["Perc"] = (x[option] / x['SNO']) * 100

    st.table(data=x)

