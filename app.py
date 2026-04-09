import streamlit as st
import pandas as pd

st.title("Data Quality Checker 🔍")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Original Data", df)

    # Missing values
    st.write("### Missing Values")
    st.write(df.isnull().sum())

    # Duplicates
    duplicates = df.duplicated().sum()
    st.write(f"Duplicate Rows: {duplicates}")

    if st.button("Clean Data"):
        df = df.drop_duplicates()
        df = df.fillna(df.mean(numeric_only=True))

        st.write("### Cleaned Data", df)
        st.success("Data Cleaned Successfully ✅")