import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="AgriLoan",
    layout="centered",
    page_icon="favicon.png",
)

# Minimize vertical space above logo
st.markdown("<div style='margin-top: -60px;'></div>", unsafe_allow_html=True)

# Load and display centered logo
logo = Image.open("AgriLoan1.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, use_container_width=False, width=180)

# Reduce vertical space below logo
st.markdown("<div style='margin-bottom: -30px;'></div>", unsafe_allow_html=True)

# Page title
st.title("Welcome to AgriLoan")

# Introductory text
st.write("""
AgriLoan is an initiative to support smallholder farmers by offering smart, AI-based loan evaluations.

We help farmers access credit more fairly by using data-driven models to assess creditworthiness.

Use the sidebar to:
- Submit a loan application
- View the admin dashboard (demo only)
""")
