import streamlit as st

# Loading APP Modules
from Modules.UI.layout_config import set_layout
from Modules.UI.header import show_header
from Modules.Utils.load_data import load_dataset

# Layout
set_layout()

# Loading Data
df = load_dataset("Data/Yelp_sampled_df.parquet")

#GUI
show_header("🧠 Business Intelligence Explorer")

st.dataframe(df.head())
