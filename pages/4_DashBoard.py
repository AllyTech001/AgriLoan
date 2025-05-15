import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="Loan Applicants Dashboard", layout="wide")

# Reload data each time the app runs or when refresh is pressed
def load_data():
    df = pd.read_excel("loan_dataset.xlsx")
    df['ApplicationDate'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
    return df


# Load dataset
df = load_data()

# Dashboard title and description
st.title("Loan Applicants Dashboard")
st.markdown("Explore applicant trends, financial data, and demographics with interactive charts.")

# Debug info: total rows loaded
st.markdown(f"**Total Applicants:** {len(df)}")

# Prepare date grouping columns for charts
df['Date'] = df['ApplicationDate'].dt.date
df['Week'] = df['ApplicationDate'].dt.to_period('W').apply(lambda r: r.start_time)
df['Month'] = df['ApplicationDate'].dt.to_period('M').apply(lambda r: r.start_time)

# Metrics
total_daily = df.groupby('Date').size().sum()
total_weekly = df.groupby('Week').size().sum()
total_monthly = df.groupby('Month').size().sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Daily Applicants (sum)", f"{total_daily}")
col2.metric("Total Weekly Applicants (sum)", f"{total_weekly}")
col3.metric("Total Monthly Applicants (sum)", f"{total_monthly}")

# Loan Amount Trend
st.subheader("Loan Amount Trend Over Time")
loan_time = df.groupby('ApplicationDate')['LoanAmount'].sum().reset_index()
st.line_chart(data=loan_time, x='ApplicationDate', y='LoanAmount')

# Education Level Distribution
st.subheader("Applicants by Education Level")
edu_counts = df['Education'].fillna("Unknown").value_counts()
st.bar_chart(edu_counts)

# Income Trend
st.subheader("Income Trend Over Time")
income_time = df.groupby('ApplicationDate')['Income'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 4))
ax.fill_between(income_time['ApplicationDate'], income_time['Income'], color='skyblue', alpha=0.5)
ax.plot(income_time['ApplicationDate'], income_time['Income'], color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Average Income")
st.pyplot(fig)

# Crop Produce Distribution
st.subheader("Crop Produce Distribution")
crop_counts = df['Crop_Produce'].value_counts()
st.bar_chart(crop_counts)

# Credit Score Distribution
st.subheader("Credit Score Distribution")
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.histplot(df['CreditScore'].dropna(), bins=20, kde=True, color='green', ax=ax2)
ax2.set_xlabel("Credit Score")
st.pyplot(fig2)

# Loan Term Distribution
st.subheader("Loan Term Distribution")
loan_term_counts = df['LoanTerm'].fillna("Unknown").value_counts().sort_index()
st.bar_chart(loan_term_counts)
