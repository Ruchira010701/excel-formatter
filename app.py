import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Formatter", layout="centered")

st.title("📊 Excel Formatter Tool")

uploaded_file = st.file_uploader(
    "Upload Excel File (.xlsx)",
    type=["xlsx"]
)

format_option = st.selectbox(
    "Select Format",
    [
        "Format 1",
        "Format 2",
        "Format 3",
        "Format 4",
        "Format 5",
        "Format 6",
        "Format 7",
        "Format 8",
        "Format 9",
    ]
)

def format_1(df):
    df.columns = [c.upper() for c in df.columns]
    return df

def format_2(df):
    df = df.dropna(how="all")
    return df

def format_3(df):
    df.insert(0, "SR_NO", range(1, len(df) + 1))
    return df

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name=0)

    if st.button("Generate File"):
        if format_option == "Format 1":
            df = format_1(df)
        elif format_option == "Format 2":
            df = format_2(df)
        elif format_option == "Format 3":
            df = format_3(df)

        df.to_excel("formatted.xlsx", index=False)

        with open("formatted.xlsx", "rb") as f:
            st.download_button(
                "⬇️ Download Formatted File",
                f,
                file_name="formatted.xlsx"
            )
