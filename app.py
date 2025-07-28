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

# Sidebar or horizontal layout for filters
# Filter widgets
col1, col2 = st.columns(2)

with col1:
    selected_state = st.selectbox("📍 Select a State", sorted(df["state"].unique()), key="selected_state")

with col2:
    selected_categories = st.multiselect("🏷️ Select Business Categories", sorted(df.columns[11:]), key="selected_categories")

# Initialize session state if not set
if "prev_selected_state" not in st.session_state:
    st.session_state.prev_selected_state = selected_state
if "prev_selected_categories" not in st.session_state:
    st.session_state.prev_selected_categories = selected_categories

# Filter data (do this regardless of trigger)
filtered_df = filter_data(df, state=selected_state, categories=selected_categories)

# Check if filters changed
filters_changed = (
    selected_state != st.session_state.prev_selected_state or
    selected_categories != st.session_state.prev_selected_categories
)

# Show map only if needed
if filters_changed:
    st.session_state.prev_selected_state = selected_state
    st.session_state.prev_selected_categories = selected_categories

    map_df = filtered_df.copy()
    if len(map_df) > 500:
        map_df = map_df.sample(500, random_state=42)

    show_business_map(map_df, state_code=selected_state)
