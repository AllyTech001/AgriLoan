import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.set_page_config(page_title="Colorful Excel Data Dashboard", layout="wide")
    st.title("🌈 Colorful Interactive Excel Dashboard")

    # Load the Excel file
    try:
        df = pd.read_excel('dataset.xlsx')
    except FileNotFoundError:
        st.error("File 'dataset.xlsx' not found in the current folder.")
        return

    # Show Data Preview
    st.subheader("📋 Data Preview")
    st.dataframe(df)

    # Show Features
    st.subheader("🧩 Features (Columns)")
    st.write(list(df.columns))

    # Show Data Types
    st.subheader("🔍 Data Types")
    st.write(df.dtypes)

    # Summary Statistics
    st.subheader("📊 Summary Statistics")
    st.write(df.describe(include='all').transpose())

    # Missing Values
    st.subheader("🚨 Missing Values Heatmap")
    missing = df.isnull()
    fig, ax = plt.subplots(figsize=(10, 3))
    sns.heatmap(missing, cbar=False, cmap='viridis', yticklabels=False, ax=ax)
    st.pyplot(fig)

    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    st.subheader("📈 Numeric Columns Analysis")

    for col in numeric_cols:
        st.markdown(f"### {col}")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # Histogram
        sns.histplot(df[col].dropna(), kde=True, color='skyblue', ax=axes[0])
        axes[0].set_title(f'Histogram of {col}')

        # Boxplot
        sns.boxplot(x=df[col], color='lightgreen', ax=axes[1])
        axes[1].set_title(f'Boxplot of {col}')

        st.pyplot(fig)

    # Correlation Heatmap
    if len(numeric_cols) > 1:
        st.subheader("🔥 Correlation Heatmap (Numeric Columns)")
        corr = df[numeric_cols].corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    st.subheader("📊 Categorical Columns Analysis")

    for col in categorical_cols:
        st.markdown(f"### {col}")
        counts = df[col].value_counts().head(20)
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.barplot(x=counts.values, y=counts.index, palette='pastel', ax=ax)
        ax.set_title(f'Top Categories in {col}')
        st.pyplot(fig)

    # Interactive Column Exploration
    st.sidebar.header("🔎 Explore Specific Column")
    selected_col = st.sidebar.selectbox("Select a column", df.columns)

    st.sidebar.markdown("---")
    st.sidebar.write(f"**Basic info about {selected_col}:**")
    st.sidebar.write(f"Data type: {df[selected_col].dtype}")
    st.sidebar.write(f"Missing values: {df[selected_col].isnull().sum()}")

    if selected_col in numeric_cols:
        st.sidebar.write("Summary stats:")
        st.sidebar.write(df[selected_col].describe())
    else:
        st.sidebar.write("Top value counts:")
        st.sidebar.write(df[selected_col].value_counts().head(10))

if __name__ == "__main__":
    main()
