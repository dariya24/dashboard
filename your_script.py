import streamlit as st
import pandas as pd

df = pd.read_csv("data/HDHI_Admission_data_post_processed.csv")

subset = df[["AGE", "GENDER", "RURAL", "ICU_admission_status", "Duration_Label", 'DURATION OF STAY',
       'duration of intensive unit stay']]


options_vars = ["GENDER", "RURAL"]


option = st.selectbox(
    "How would you like to be contacted?",
    options_vars,
)

if st.checkbox('Only ICU Admissions'):
    second_var = "duration of intensive unit stay"
else:
    second_var = "DURATION OF STAY"

st.bar_chart(subset[[second_var, option]])




x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



st.write("You selected:", option)

