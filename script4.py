import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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


with st.container():

    option = st.selectbox(
        "Which laboratory results you want to review?",
        labs,
    )


    if st.checkbox('Only ICU Admissions'):
        subset = df[df.ICU_admission_status == 1]
    else:
        subset = df


    subset.pivot(columns='Duration_Label', values=option).plot.hist(alpha=0.5, title=option, bins=50)

    # Show the plot in Streamlit
    st.pyplot(plt)





with st.container():

    conditions = ["SMOKING","ALCOHOL","Diabetes Mellitus","Hypertension","Coronary Artery Disease","PRIOR CARDIOMYOPATHY","CHRONIC KIDNEY DISEASE"]

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

