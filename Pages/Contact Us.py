import streamlit as st

# Must be at the very top
st.set_page_config(
    page_title="Contact Us:",     # Appears in browser tab
    page_icon="favicon.png",                      # Favicon (can be emoji or image)
    layout="wide"                        # "centered" or "wide"
)
st.title("📬 Contact Page")
st.write("Reach us at: contact@example.com")
