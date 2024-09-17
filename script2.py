import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you already have a DataFrame called 'df' with columns:
# 'age', 'days_stayed_in_the_hospital', and 'group_label'

# Sample DataFrame for demonstration (replace this with your actual data)
data = {
    'age': [23, 45, 56, 67, 34, 78, 50, 45, 37, 65],
    'days_stayed_in_the_hospital': [4, 6, 2, 8, 3, 9, 1, 7, 5, 3],
    'group_label': ['A', 'B', 'A', 'A', 'B', 'C', 'C', 'B', 'C', 'A']
}

df = pd.DataFrame(data)

# Create the Streamlit app
st.title("Days Stayed in the Hospital Distribution by Group")

# Create a figure
plt.figure(figsize=(10,6))

# Create the histogram using seaborn, color-coded by 'group_label'
sns.histplot(data=df, x='days_stayed_in_the_hospital', hue='group_label')

# Set plot labels
plt.title('Distribution of Days Stayed in the Hospital by Group Label')
plt.xlabel('Days Stayed in the Hospital')
plt.ylabel('Frequency')

# Show the plot in Streamlit
st.pyplot(plt)