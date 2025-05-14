# import streamlit as st
# st.title("🏠 Home Page")
# st.write("Welcome to the home page of our Streamlit multipage app!")
# st.sidebar.image("AgriLoan.png", use_container_width=True)
# st.sidebar.markdown("### Farmware.")
# st.sidebar.markdown("_Smart Farming Made Simple_")

import streamlit as st

# Must be at the very top
st.set_page_config(
    page_title="AgriLoan",     # Appears in browser tab
    page_icon="favicon.png",                      # Favicon (can be emoji or image)
    layout="wide"                        # "centered" or "wide"
)

st.title("Farmware Dashboard")
st.write("Welcome to the smart farming system.")
