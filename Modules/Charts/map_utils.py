import folium
import streamlit as st
from streamlit_folium import st_folium

def show_business_map(df, state_code=None, map_center=None, zoom=7):
    """
    Show a map of business locations using latitude and longitude.
    Preserves zoom and center if provided.
    """
    if df.empty:
        st.warning("No businesses to display on the map.")
        return None, map_center, zoom

    # Fallback if map_center is None
    if map_center is None:
        map_center = [df["latitude"].mean(), df["longitude"].mean()]

    # Initialize map
    m = folium.Map(location=map_center, zoom_start=zoom)

    # Add markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row.get("name", "Unnamed"),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    st.markdown(f"### 📍 Business Locations in {state_code or 'Selected Region'}")
    map_data = st_folium(m, width=800, height=500)

    # Extract updated view (fallback to current if not found)
    new_center = map_data.get("center", map_center)
    new_zoom = map_data.get("zoom", zoom)

    return m, new_center, new_zoom
