import streamlit as st

# Loading APP Modules
from Modules.UI.header import show_header
from Modules.Utils.load_data import load_dataset

# Loading Data
df = load_dataset("Data/Yelp_sampled_df.parquet")

#GUI
show_header("🧠 Business Intelligence Explorer")

st.dataframe(df.head())
