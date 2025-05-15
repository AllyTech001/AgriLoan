import streamlit as st
import pandas as pd
import random
import string
import os
import time
from datetime import datetime
from fpdf import FPDF

# Constants
EXCEL_FILE = 'loan_dataset.xlsx'
PROFILE_FILE = 'profile_details.xlsx'
LOGO_FILE = 'AgriLoan.png'
NAIRA = "₦"

# Generate unique 8-char alphanumeric LoanID
def generate_loan_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Create PDF receipt
def create_pdf(full_name, bvn, phone_number, loan_id, output_file):
    pdf = FPDF()
    pdf.add_page()

    if os.path.exists(LOGO_FILE):
        pdf.image(LOGO_FILE, x=10, y=8, w=40)

    pdf.set_xy(0, 20)
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 20, "Loan Application Receipt", ln=True, align='C')

    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, "Thank you for applying with AgriLoan.", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(50, 10, "Full Name:", ln=0)
    pdf.set_font("Arial", '', 14)
    pdf.cell(0, 10, full_name, ln=1)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(50, 10, "BVN Number:", ln=0)
    pdf.set_font("Arial", '', 14)
    pdf.cell(0, 10, bvn, ln=1)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(50, 10, "Phone Number:", ln=0)
    pdf.set_font("Arial", '', 14)
    pdf.cell(0, 10, phone_number, ln=1)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(50, 10, "Loan ID:", ln=0)
    pdf.set_font("Arial", '', 14)
    pdf.cell(0, 10, loan_id, ln=1)

    pdf.ln(15)

    pdf.set_font("Arial", 'I', 10)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f"Submission Timestamp: {timestamp}", ln=1, align='R')

    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y() + 5, 200, pdf.get_y() + 5)

    pdf.output(output_file)

# Initialize session state with correct types and defaults
def init_session_state():
    defaults = {
        "full_name": "",
        "bvn": "",
        "phone_number": "",
        "age": 18,
        "income": 0.0,
        "loan_amount": 0.0,
        "credit_score": 300,
        "experience": 0,
        "interest_rate": 0.0,
        "loan_term": 1,
        "education": "None",
        "has_collateral": False,
        "has_dependents": False,
        "has_cosigner": False,
        "farm_size": 0.1,
        "crop_produce": "",
        "annual_return": 0.0,
    }
    for key, default in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default

# Main Streamlit app
def main():
    st.set_page_config(page_title="Loan Data Entry", layout="centered")
    st.title("AgriLoan Application Form")

    init_session_state()

    with st.form("loan_form"):
        st.subheader("Enter Applicant Details")

        full_name = st.text_input("Full Name*", key="full_name")
        bvn = st.text_input("Bank Verification Number (BVN)*", key="bvn")
        phone_number = st.text_input("Phone Number*", key="phone_number")
        age = st.number_input("Age", min_value=18, max_value=100, step=1, key="age")
        income = st.number_input(f"Annual Income ({NAIRA})", min_value=0.0, step=1000.0, key="income")
        loan_amount = st.number_input(f"Loan Amount ({NAIRA})*", min_value=0.0, step=1000.0, key="loan_amount")
        credit_score = st.slider("Credit Score", min_value=300, max_value=850, key="credit_score")
        experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1, key="experience")
        interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, step=0.1, key="interest_rate")
        loan_term = st.selectbox(
            "Loan Term (Years)", options=[1, 2, 3, 5, 10], index=[1,2,3,5,10].index(st.session_state.loan_term),
            key="loan_term"
        )
        education = st.selectbox(
            "Education Level",
            options=["None", "Primary", "Secondary", "Tertiary"],
            index=["None", "Primary", "Secondary", "Tertiary"].index(st.session_state.education),
            key="education"
        )
        has_collateral = st.checkbox("Has Collateral?", key="has_collateral")
        has_dependents = st.checkbox("Has Dependents?", key="has_dependents")
        has_cosigner = st.checkbox("Has Co-Signer?", key="has_cosigner")
        farm_size = st.number_input("Farm Size (Acre)*", min_value=0.1, step=0.1, key="farm_size")
        crop_produce = st.text_input("Main Crop Produce", key="crop_produce")
        annual_return = st.number_input(f"Estimated Annual Return ({NAIRA})*", min_value=0.0, step=1000.0, key="annual_return")

        submitted = st.form_submit_button("Submit")

    if submitted:
        # Validate required fields
        if not full_name.strip() or not bvn.strip() or not phone_number.strip() \
                or loan_amount == 0 or annual_return == 0:
            st.error("Please fill all required fields: Full Name, BVN, Phone Number, Loan Amount, and Annual Return.")
            return

        loan_id = generate_loan_id()
        new_entry = {
            'LoanID': loan_id,
            'FullName': full_name,
            'BVN': bvn,
            'PhoneNumber': phone_number,
            'Age': age,
            'Income': income,
            'LoanAmount': loan_amount,
            'CreditScore': credit_score,
            'Experience': experience,
            'InterestRate': interest_rate,
            'LoanTerm': loan_term,
            'Education': education,
            'HasCollateral': has_collateral,
            'HasDependents': has_dependents,
            'HasCoSigner': has_cosigner,
            'Farm_Size(Acre)': farm_size,
            'Crop_Produce': crop_produce,
            'AnnualReturn': annual_return
        }

        # Save to loan dataset excel
        if os.path.exists(EXCEL_FILE):
            df_existing = pd.read_excel(EXCEL_FILE)
            df_updated = pd.concat([df_existing, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            df_updated = pd.DataFrame([new_entry])
        df_updated.to_excel(EXCEL_FILE, index=False)

        # Save profile details to separate Excel (append if exists)
        profile_entry = {
            'LoanID': loan_id,
            'FullName': full_name,
            'BVN': bvn,
            'PhoneNumber': phone_number
        }
        if os.path.exists(PROFILE_FILE):
            df_profile = pd.read_excel(PROFILE_FILE)
            df_profile_updated = pd.concat([df_profile, pd.DataFrame([profile_entry])], ignore_index=True)
        else:
            df_profile_updated = pd.DataFrame([profile_entry])
        df_profile_updated.to_excel(PROFILE_FILE, index=False)

        with st.spinner("Processing your submission..."):
            time.sleep(2)

        st.success(f"Entry submitted successfully! ✅ Loan ID: `{loan_id}`")
        st.write("📧 The applicant will be contacted via email with further details.")

        # Generate PDF receipt
        pdf_file = f"{loan_id}_receipt.pdf"
        create_pdf(full_name, bvn, phone_number, loan_id, pdf_file)

        # Download PDF button
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📄 Download Receipt PDF",
                data=f,
                file_name=pdf_file,
                mime="application/pdf"
            )

        st.info("To submit another application, please refresh the page.")

if __name__ == "__main__":
    main()
