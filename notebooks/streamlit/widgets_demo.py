
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date

st.title("Interactive Widgets Demo")

st.header("Input Widgets")

# Text input
name = st.text_input("What's your name?", value="Enter your name here")
st.write(f"Hello, {name}!")

# Number input
age = st.number_input("How old are you?", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old.")

# Slider
temperature = st.slider("Select temperature", min_value=-10, max_value=40, value=20)
st.write(f"Temperature: {temperature}°C")

# Select box
option = st.selectbox("Choose your favorite color", 
                     ["Red", "Green", "Blue", "Yellow"])
st.write(f"Your favorite color is {option}")

# Multi-select
options = st.multiselect("Choose multiple options",
                        ["Option 1", "Option 2", "Option 3", "Option 4"],
                        default=["Option 1", "Option 2"])
st.write(f"You selected: {options}")

# Radio buttons
genre = st.radio("What's your favorite movie genre?",
                ["Comedy", "Drama", "Documentary"])
st.write(f"You selected: {genre}")

# Checkbox
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.success("Thanks for agreeing!")

# Date input
birthday = st.date_input("When is your birthday?", 
                        value=date(1990, 1, 1))
st.write(f"Your birthday is: {birthday}")

# Time input
time = st.time_input("What time is it?")
st.write(f"Time: {time}")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File uploaded successfully!")
    st.dataframe(df.head())

# Button
if st.button("Click me!"):
    st.balloons()
    st.success("Button clicked!")
