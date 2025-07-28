import streamlit as st

# Loading APP Modules
from Modules.UI.layout_config import set_layout
from Modules.UI.header import show_header
from Modules.Utils.load_data import load_dataset
from Modules.Utils.filter_data import filter_data
from Modules.Utils.export_data import download_filtered_data
from Modules.Charts.map_utils import show_business_map
from Modules.Charts.bar_plot import bar_plotly
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

# ---- Data Filtering (always needed for table + export) ----
filtered_df = filter_data(df, state=selected_state, categories=selected_categories)
filtered_df.reset_index(drop=True, inplace=True)

# ---- Show Filtered Table ----
st.markdown(f"### Showing results for `{selected_state}` with selected categories: {len(filtered_df)} Total number of Observations")
st.dataframe(filtered_df[["name", "city", "stars", "review_count"]], height=200)

# Layout side by side
col_map, col_chart = st.columns([1, 2])  # Adjust ratio as needed

# ---- Left Column: Map ----
with col_map:
    st.markdown("## 🗺️ Business Locations Map")
    st.caption("Only up to 500 businesses are displayed to avoid rendering issues.")
    map_df = filtered_df.copy()
    if len(map_df) > 500:
        map_df = map_df.sample(500, random_state=42)
    show_business_map(map_df, state_code=selected_state)

# ---- Right Column: Category Frequency Bar Chart ----
with col_chart:
    category_counts = filtered_df.iloc[:, 11:].sum().sort_values(ascending=False)
    # Slider to select starting index
    max_start = max(0, len(category_counts) - 20)
    start_index = st.slider("🔢 Start Index for Displayed Businesses", 0, max_start, 0)
    
    st.markdown("## 📊 Business Composition according to the selected data")
    bar_plotly(category_counts.iloc[start_index:start_index+20])
    # ---- Export Button ----
    st.caption("You can export your data here:")
    download_filtered_data(filtered_df, state_code=selected_state)
