import streamlit as st
from PIL import Image


st.set_page_config(page_title="AgriLoan", 
                   layout="centered",
                   page_icon="favicon.png",)

# Load the image
logo = Image.open("AgriLoan1.png")

# Center the image and reduce its size to a "standard" width (e.g. 200px)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, use_container_width=False, width=200)  # Set width to a standard size (200px)

st.title("Welcome to AgriLoan")

st.write("""
AgriLoan is an initiative to support smallholder farmers by offering smart, AI-based loan evaluations.

We help farmers access credit more fairly by using data-driven models to assess creditworthiness.

Use the sidebar to:
- Submit a loan application
- View the admin dashboard (demo only)
""")
