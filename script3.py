import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming you already have a DataFrame called 'df' with columns:
# 'age', 'days_stayed_in_the_hospital', and 'group_label'

# Sample DataFrame for demonstration (replace this with your actual data)
data = {
    'age': [23, 45, 56, 67, 34, 78, 50, 45, 37, 65],
    'days_stayed_in_the_hospital': [4, 6, 2, 8, 3, 9, 1, 7, 5, 3],
    'group_label': ['A', 'B', 'A', 'A', 'B', 'C', 'C', 'B', 'C', 'A']
}

df = pd.DataFrame(data)

# Streamlit app title
st.title("Interactive Distribution of Days Stayed in the Hospital by Group")

# Create an interactive histogram using Plotly
fig = px.histogram(
    df,
    x='days_stayed_in_the_hospital',
    color='group_label',
    labels={'days_stayed_in_the_hospital': 'Days Stayed in the Hospital', 'group_label': 'Group'},
    title='Distribution of Days Stayed in the Hospital by Group Label',
    barmode='overlay',
    nbins=10,  # Number of bins
    histnorm='count',  # Could be 'percent' if you want a normalized histogram
)

# Update layout for better visualization
fig.update_layout(
    xaxis_title='Days Stayed in the Hospital',
    yaxis_title='Count',
    bargap=0.1  # Adjusts gap between bars
)

# Show the plot in Streamlit
st.plotly_chart(fig)