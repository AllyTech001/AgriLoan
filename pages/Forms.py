import streamlit as st

# Must be at the very top
st.set_page_config(
    page_title="Form:",     # Appears in browser tab
    page_icon="favicon.png",                      # Favicon (can be emoji or image)
    layout="wide"                        # "centered" or "wide"
)
st.title("Submit your details")
st.write("Please fill out the form below:")
