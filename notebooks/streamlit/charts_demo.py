
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Data Visualization with Streamlit")

# Load the penguins dataset
penguins_df = pd.read_csv('../data/penguins.csv')

st.header("Dataset Preview")
st.write("Here's our penguins dataset:")
st.dataframe(penguins_df.head())

# Remove rows with missing values for visualization
penguins_clean = penguins_df.dropna()

st.header("Built-in Streamlit Charts")

# Line chart
st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Area chart
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar chart
st.subheader("Bar Chart")
species_counts = penguins_clean['species'].value_counts()
st.bar_chart(species_counts)

# Scatter plot
st.subheader("Scatter Plot")
scatter_data = penguins_clean[['bill_length_mm', 'bill_depth_mm']]
st.scatter_chart(scatter_data, x='bill_length_mm', y='bill_depth_mm')

st.header("Matplotlib Integration")
fig, ax = plt.subplots()
ax.scatter(penguins_clean['bill_length_mm'], penguins_clean['flipper_length_mm'])
ax.set_xlabel('Bill Length (mm)')
ax.set_ylabel('Flipper Length (mm)')
ax.set_title('Bill Length vs Flipper Length')
st.pyplot(fig)

st.header("Plotly Integration")
fig = px.scatter(penguins_clean, 
                x='bill_length_mm', 
                y='bill_depth_mm',
                color='species',
                title='Bill Dimensions by Species')
st.plotly_chart(fig)
