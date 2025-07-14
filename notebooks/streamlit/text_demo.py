
import streamlit as st

st.title("Text and Formatting Demo")

# Different text elements
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is plain text")

# Markdown formatting
st.markdown("""
### This is markdown
- **Bold text**
- *Italic text*
- `Code text`
- [Link to Streamlit](https://streamlit.io)
""")

# Code blocks
st.code("""
def hello():
    print("Hello, Streamlit!")
""", language='python')

# LaTeX
st.latex(r"""e^{i\pi} + 1 = 0""")

# Success, info, warning, error messages
st.success("This is a success message!")
st.info("This is an info message.")
st.warning("This is a warning message.")
st.error("This is an error message.")
