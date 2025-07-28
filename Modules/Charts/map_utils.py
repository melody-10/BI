import folium
import streamlit as st
from streamlit_folium import st_folium

def show_business_map(df, state_code=None, map_center=None, zoom=7):
    """
    Show a map of business locations using latitude and longitude.

    Parameters:
    - df (pd.DataFrame): DataFrame containing 'latitude', 'longitude', and optionally 'name'.
    - state_code (str): Optional, used for display purposes.
    - map_center (tuple or None): If None, compute from df.
    - zoom (int): Zoom level to reuse.
    
    Returns:
    - map_data, new_center (tuple), new_zoom (int)
    """

    if df.empty or "latitude" not in df.columns or "longitude" not in df.columns:
        st.warning("No valid location data to display on the map.")
        return None, map_center, zoom

    # Compute map center if not provided
    if map_center is None:
        lat_center = df["latitude"].mean()
        lon_center = df["longitude"].mean()
        map_center = (lat_center, lon_center)

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
    map_data = st_folium(m, width=800, height=500, returned_objects=["center", "zoom"])

    new_center = tuple(map_data["center"]) if map_data.get("center") else map_center
    new_zoom = map_data["zoom"] if map_data.get("zoom") else zoom

    return map_data, new_center, new_zoom
