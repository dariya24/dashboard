import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dashboard_libraries import get_pvalue_propotion, prepare_dataframe_for_descriptive_analytics
import plotly.figure_factory as ff


st.set_page_config(
    page_title="PRAIS - Descriptive",
    page_icon="❤",
)

st.sidebar.image("./assets/P R A I S.png",)


df = pd.read_csv("data/HDHI_Admission_data_post_processed.csv")

df = prepare_dataframe_for_descriptive_analytics(df)


st.header("Demographic information")

st.write("In this section the overview of the demographic in the dataset is presented")


with st.container():
    st.markdown("*Select this check box to only see results for patients who were admitted to ICU*")
    if st.checkbox('Only ICU Admissions '):

        subset = df[df.ICU_admission_status == 1]
    else:
        subset = df


    # Group by 'Duration_Label' and 'GENDER' and count unique 'SNO'
    grouped_df = subset.groupby(['Length of stay', 'Gender']).agg({'SNO': pd.Series.nunique}).reset_index()

    # Rename the column to 'Unique_Encuonters_Count'
    grouped_df = grouped_df.rename(columns={'SNO': 'Number of Unique Encounters'})

    # Calculate total unique SNO for each Duration_Label
    total_counts = subset.groupby('Length of stay')['SNO'].nunique().reset_index().rename(
        columns={'SNO': 'Total Unique Encounters'})

    # Merge with grouped data
    merged_df = pd.merge(grouped_df, total_counts, on='Length of stay')

    # Calculate proportion of each gender within every Duration_Label
    merged_df['Proportion'] = merged_df['Number of Unique Encounters'] / merged_df['Total Unique Encounters']
    merged_df['Proportion'] = merged_df['Proportion'].apply(lambda x: "{}%".format(round(x * 100, 1)))

    merged_df.drop(columns=['Total Unique Encounters'], inplace=True)
    st.table(data=merged_df.sort_values(by="Length of stay", ascending=False))


    # Group by 'Duration_Label' and 'Rural or urban' and count unique 'SNO'
    grouped_df = subset.groupby(['Length of stay', 'Rural or Urban']).agg({'SNO': pd.Series.nunique}).reset_index()

    # Rename the column to 'Unique_Encuonters_Count'
    grouped_df = grouped_df.rename(columns={'SNO': 'Number of Unique Encounters'})

    # Calculate total unique SNO for each Duration_Label
    total_counts = subset.groupby('Length of stay')['SNO'].nunique().reset_index().rename(
        columns={'SNO': 'Total Unique Encounters'})

    # Merge with grouped data
    merged_df = pd.merge(grouped_df, total_counts, on='Length of stay')

    # Calculate proportion of each gender within every Duration_Label
    merged_df['Proportion'] = merged_df['Number of Unique Encounters'] / merged_df['Total Unique Encounters']

    merged_df['Proportion'] = merged_df['Proportion'].apply(lambda x: "{}%".format(round(x*100, 1)))

    merged_df.drop(columns=['Total Unique Encounters'], inplace=True)
    st.table(data=merged_df.sort_values(by="Length of stay", ascending=False))

    x1 = df[df["Length of stay"] == "Less than 7 days"].Age
    x2 = df[df["Length of stay"] == "7 or more days"].Age
    # Group data together
    hist_data = [x1, x2]

    group_labels = ['Less than 7 days', '7 or more days']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels)

    # Add title
    fig.update_layout(title_text='Age Distribution')

    # Plot!
    st.plotly_chart(fig, use_container_width=True)
    #subset.pivot(columns='Length of stay', values="Age").plot.hist(alpha=0.5, title="Age Distribution", bins=50)
    #st.pyplot(plt)


st.header("Laboratory results")

st.write("In this section the investigation of the laboratory tests results for various patient subgroups can be investigated")


labs = ["Haemoglobin","Total Leukocytes Count","Platelets","Glucose","Urea,Creatinine"]



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

st.markdown("*Select this check box to only see results for patients who were admitted to ICU*")
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
subset.dropna(inplace=True)

number_encounters = subset.SNO.nunique()
total_number_encounters = df.SNO.nunique()
mean_value = subset[option].mean()
median_value = subset[option].median()

st.subheader("Results overview")

st.write("Number of encounters: {0:.0f}".format(number_encounters))
st.write("Percentage of all encounters in the dataset that satisfy selected filters: {0:.1f}".format(100*number_encounters/total_number_encounters))
st.write("Mean {} laboratory test value: {:.1f}".format(option, mean_value))
st.write("Median {} laboratory test value: {:.1f}".format(option, median_value))


x1 = df[df["Length of stay"] == "Less than 7 days"][option]
x2 = df[df["Length of stay"] == "7 or more days"][option]
# Group data together
hist_data = [x1, x2]

group_labels = ['Less than 7 days', '7 or more days']

# Create distplot with custom bin_size
fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[0.5, 0.5])

# Add title
fig.update_layout(title_text='{} Distribution'.format(option))

# Plot!
st.plotly_chart(fig, use_container_width=True)



#col1, col2 = st.columns(2)

#with col1:

#subset.pivot(columns='Length of stay', values=option).plot.hist(alpha=0.5, title=option, bins=50)

# Show the plot in Streamlit
#st.pyplot(plt)


#with col2:
#
#    reference_values = pd.DataFrame(np.array([["<18", "X", "X"], ["18-35", "X", "X"], ["35-65", "X", "X"], ["65+", "X", "X"]]),
#                 columns=['Age Group', 'Male', 'Female'])
#
#    st.write("Reference value for: {}".format(option))
#    st.table(data=reference_values)

st.header("Comorbidities")
st.write("In this section the investigation of the comorbidities for various patient subgroups can be investigated")

with st.container():

    #conditions = ["boolGender", "boolRural", "SMOKING ","ALCOHOL","Diabetes Mellitus","Hypertension","Coronary Artery Disease","PRIOR CARDIOMYOPATHY","CHRONIC KIDNEY DISEASE"]


    conditions = ['Smoking ', 'Alcohol', 'Diabetes Mellitus', 'Hypertension', 'Coronary Artery Disease', 'Prior Cardiomyopathy', 'Chronic Kidney Disease',
                  'Severe Anaemia', 'Anaemia', 'Stable Angina', 'Acute Coronary Syndrome',
'St Elevation Myocardial Infarction', 'Atypical Chest Pain', 'Heart Failure', 'Heart Failure With Reduced Ejection Fraction',
                  'Heart Failure With Normal Ejection Fraction', 'Valvular Heart Disease', 'Complete Heart Block', 'Sick Sinus Syndrome',
                  'Acute Kidney Injury', 'Cerebrovascular Accident Infract', 'Cerebrovascular Accident Bleed', 'Atrial Fibrilation',
                  'Ventricular Tachycardia', 'Paroxysmal Supra Ventricular Tachycardia', 'Congenital Heart Disease',
                  'Urinary Tract Infection', 'Neuro Cardiogenic Syncope', 'Orthostatic', 'Infective Endocarditis',
                  'Deep Venous Thrombosis', 'Cardiogenic Shock', 'Shock', 'Pulmonary Embolism', 'Chest Infection']


    option = st.selectbox(
        "Which comorbidity you want to review?",
        conditions,
    )

    #Charts don't make sense here, because it is hard to see trends
    #subset.pivot(columns='Duration_Label', values=option).plot.hist(alpha=0.5, title=option, bins=50)
    # Show the plot in Streamlit
    # st.pyplot(plt)

    st.markdown("*Select this check box to only see results for patients who were admitted to ICU*")
    if st.checkbox('Only ICU Admissions  '):
        only_ICU1 = 1
        subset = df[df.ICU_admission_status == 1]
    else:
        only_ICU1 = 0
        subset = df

    st.write("The tables below show the number and proportion of individuals with selected comorbidity")
    st.write("Statistically significant comorbidities are colored green and others - red")

    st.subheader("Comparison of {} for different length of stay".format(option))

    a = subset.groupby("Length of stay")[option].sum().reset_index()
    b = subset.groupby("Length of stay").SNO.count()
    x = pd.merge(a, b, on="Length of stay")
    x["Proportion"] = (x[option] / x['SNO']) * 100
    x["Proportion"] = x["Proportion"].apply(lambda x: "{}%".format(round(x)))
    x.drop(columns={"SNO"}, inplace=True)
    st.table(data=x.sort_values(by="Length of stay", ascending=False))

    text, color = get_pvalue_propotion(subset, option, "Length of stay")
    st.write(":{}[{}]".format(color, text))

    st.subheader("Comparison of {} for different ICU Admission".format(option))

    a = subset.groupby("ICU_admission_status")[option].sum().reset_index()
    b = subset.groupby("ICU_admission_status").SNO.count()
    x = pd.merge(a, b, on="ICU_admission_status")
    x["Proportion"] = (x[option] / x['SNO']) * 100
    x["Proportion"] = x["Proportion"].apply(lambda x: "{}%".format(round(x)))
    x.drop(columns={"SNO"}, inplace=True)

    x["ICU_admission_status"] = x["ICU_admission_status"].apply(lambda x: "Admitted to ICU" if x == 1 else "Not admitted to ICU")
    x.rename(columns={"ICU_admission_status": "ICU Admission Status"})
    st.table(data=x)




    # If only ICU, then we can not calculate percentage, therefore only do this line below if NOT ICU
    if not only_ICU1:
        text, color = get_pvalue_propotion(subset, option, "ICU_admission_status")
        st.write(":{}[{}]".format(color, text))


import plotly
print(plotly.__version__)