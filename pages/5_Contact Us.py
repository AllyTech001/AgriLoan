import streamlit as st

st.set_page_config(
    page_title="Contact Us:",     # Appears in browser tab
    page_icon="favicon.png",      # Favicon (can be emoji or image)
    layout="wide"                 # "centered" or "wide"
)


def contact_us_page():
    st.title("Contact Us")
    st.write("We'd love to hear from you! Please fill out the form below and we'll get back to you shortly.")

    with st.form(key='contact_form'):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        subject = st.text_input("Subject")
        message = st.text_area("Message")

        submit_button = st.form_submit_button(label='Send Message')

    if submit_button:
        if not name or not email or not subject or not message:
            st.error("Please fill out all fields before submitting.")
        else:
            
            st.success(f"Thank you, {name}! Your message has been sent successfully. We'll get back to you soon.")

if __name__ == "__main__":
    contact_us_page()
