
import streamlit as st

# Title of the app
st.title("My First Streamlit App! 🎉")

# Header
st.header("Welcome to Streamlit")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is some text.")

# Markdown
st.markdown("**This is bold text** and *this is italic text*")

# Write (automatically detects data type)
st.write("Hello, World!")
st.write(1234)
st.write([1, 2, 3, 4])
