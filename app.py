import streamlit as st

# Loading APP Modules
from Modules.UI.layout_config import set_layout
from Modules.UI.header import show_header
from Modules.Utils.load_data import load_dataset
from Modules.Utils.filter_data import filter_data

# Layout
set_layout()

# Load Data
df = load_dataset("Data/Yelp_sampled_df.parquet")

# Show Header
show_header("🧠 Business Intelligence Explorer")

# Sidebar or horizontal layout for filters
col1, col2 = st.columns(2)

with col1:
    selected_state = st.selectbox("📍 Select a State", sorted(df["state"].unique()))

with col2:
    selected_categories = st.multiselect("🏷️ Select Business Categories", sorted(df.columns[11:]))

# Filter Data
filtered_df = filter_data(df, state=selected_state, categories=selected_categories)

# Show filtered data
st.markdown(f"### Showing results for `{selected_state}` with selected categories: {} Total number of Observations".format(len(filtered_df))
st.dataframe(filtered_df.head(10))
