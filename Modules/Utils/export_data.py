import streamlit as st
import io
import pandas as pd

def download_filtered_data(df: pd.DataFrame, state_code: str = "selection"):
    """
    Display a download button for the filtered DataFrame as a CSV file.

    Parameters:
    - df (pd.DataFrame): The filtered DataFrame to download.
    - state_code (str): Used to name the output file.
    """
    if df.empty:
        st.info("No data available to download.")
        return

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_buffer.getvalue(),
        file_name=f"filtered_yelp_{state_code}.csv",
        mime="text/csv"
    )
