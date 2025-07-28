import streamlit as st

# Loading APP Modules
from Modules.UI.layout_config import set_layout
from Modules.UI.header import show_header
from Modules.Utils.load_data import load_dataset
from Modules.Utils.filter_data import filter_data
from Modules.Charts.map_utils import show_business_map
from Modules.Utils.export_data import download_filtered_data
from streamlit_folium import st_folium

# Layout
set_layout()

# Load Data
df = load_dataset("Data/Yelp_sampled_df.parquet")

# Show Header
show_header("🧠 Business Intelligence Explorer")

# Filter Widgets
col1, col2 = st.columns(2)

with col1:
    selected_state = st.selectbox("📍 Select a State", sorted(df["state"].unique()), key="selected_state")

with col2:
    selected_categories = st.multiselect("🏷️ Select Business Categories", sorted(df.columns[11:]), key="selected_categories")

# ---- Session State Initialization ----
if "prev_selected_state" not in st.session_state:
    st.session_state.prev_selected_state = selected_state
if "prev_selected_categories" not in st.session_state:
    st.session_state.prev_selected_categories = selected_categories.copy()

# ---- Data Filtering (always needed for table + export) ----
filtered_df = filter_data(df, state=selected_state, categories=selected_categories)
filtered_df.reset_index(drop=True, inplace=True)

# ---- Export Button ----
download_filtered_data(filtered_df, state_code=selected_state)

# ---- Show Filtered Table ----
st.markdown(f"### Showing results for `{selected_state}` with selected categories: {len(filtered_df)} Total number of Observations")
st.dataframe(filtered_df[["name", "city", "stars", "review_count"]], height=200)

# ---- Show Map if filters changed ----
filters_changed = (
    selected_state != st.session_state.prev_selected_state or
    tuple(sorted(selected_categories)) != tuple(sorted(st.session_state.prev_selected_categories))
)

if filters_changed:
    st.session_state.prev_selected_state = selected_state
    st.session_state.prev_selected_categories = selected_categories.copy()

    map_df = filtered_df.copy()
    if len(map_df) > 500:
        map_df = map_df.sample(500, random_state=42)

    st.markdown("## 🗺️ Business Locations Map")
    st.caption("Only up to 500 businesses are displayed to avoid rendering issues.")
    show_business_map(map_df, state_code=selected_state)
