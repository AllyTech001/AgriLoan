import streamlit as st

st.set_page_config(page_title="Creditworthiness Tips", 
                   page_icon="favicon.png", 
                   layout="centered")

# Optional: Custom CSS for styling (you can include this once globally in your main page too)
st.markdown(
    """
    <style>
    .tip-card {
        background-color: #f9f9f9;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .tip-card h4 {
        color: #1a6d3d;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌾 Tips to Improve Farmer Creditworthiness")

st.write("""
Helping farmers become more creditworthy increases their chances of receiving fair and timely loans.
Here are practical, proven tips that farmers can apply to build a strong financial reputation.
""")

# Tips
tips = [
    {
        "title": "1. Keep Accurate Farm Records",
        "content": "Maintain detailed records of harvests, input costs, sales, and expenses. Lenders favor farmers who can demonstrate financial literacy and transparency."
    },
    {
        "title": "2. Diversify Income Sources",
        "content": "Farmers who engage in other income-generating activities—like poultry, agro-processing, or seasonal labor—are seen as less risky."
    },
    {
        "title": "3. Join a Cooperative or Farmer Group",
        "content": "Being part of a group provides social and financial support. It also increases access to group loans and better lending terms."
    },
    {
        "title": "4. Use Inputs Efficiently",
        "content": "Practicing good agronomy—like timely planting, correct fertilizer application, and pest control—leads to better yields and more reliable income."
    },
    {
        "title": "5. Build a Relationship with Financial Institutions",
        "content": "Open a bank or mobile money account. Regular transactions build a financial history that lenders can assess."
    },
    {
        "title": "6. Attend Financial Literacy Trainings",
        "content": "Understanding budgeting, saving, and borrowing boosts credibility. Many NGOs and banks offer free training sessions."
    },
    {
        "title": "7. Repay Previous Loans on Time",
        "content": "Timely loan repayment builds trust and makes future borrowing easier and cheaper."
    }
]

# Display each tip in a styled card
for tip in tips:
    st.markdown(f"""
    <div class="tip-card">
        <h4>{tip['title']}</h4>
        <p>{tip['content']}</p>
    </div>
    """, unsafe_allow_html=True)
