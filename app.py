import streamlit as st

# Loading APP Modules
from Modules.UI.layout_config import set_layout
from Modules.UI.header import show_header
from Modules.Utils.load_data import load_dataset
from Modules.Utils.filter_data import filter_data
from Modules.Charts.map_utils import show_state_map
from streamlit_folium import st_folium

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
filtered_df.reset_index(drop=True, inplace=True)

# Show filtered data
st.markdown(f"### Showing results for `{selected_state}` with selected categories: {len(filtered_df)} Total number of Observations")
st.dataframe(filtered_df, height=200)

# Map Visualization
st.markdown("## 🗺️ Business Locations Map")

map_object = show_state_map(selected_state, filtered_df)

if map_object:
    st_folium(map_object, width=700, height=500)
