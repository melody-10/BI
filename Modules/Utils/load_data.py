# BI/Modules/Utils/load_data.py

import pandas as pd
import streamlit as st

@st.cache_data(show_spinner="Loading dataset...")
def load_dataset(parquet_path: str) -> pd.DataFrame:
    """
    Load the Yelp cleaned dataset from a Parquet file and cache it for performance.

    Parameters:
    -----------
    parquet_path : str
        Path to the Parquet file.

    Returns:
    --------
    pd.DataFrame
        Loaded DataFrame.
    """
    df = pd.read_parquet(parquet_path)
    return df
