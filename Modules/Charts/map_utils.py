import folium
import streamlit as st
from streamlit_folium import st_folium

def show_business_map(df, state_code=None, map_center=None, zoom=7):
    """
    Show a map of business locations using latitude and longitude.

    Parameters:
    - df (pd.DataFrame): DataFrame containing 'latitude', 'longitude', and optionally 'name'.
    - state_code (str): Optional, used for display purposes.
    - map_center (tuple): Tuple (lat, lon) to center the map on.
    - zoom (int): Zoom level to reuse.
    """

    if df.empty:
        st.warning("No businesses to display on the map.")
        return None, map_center, zoom

    # Center on the selected view or recompute
    if map_center is None:
        lat_center = df["latitude"].mean()
        lon_center = df["longitude"].mean()
        map_center = (lat_center, lon_center)

    # Initialize map with preserved zoom and center
    m = folium.Map(location=map_center, zoom_start=zoom)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row.get("name", "Unnamed"),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    st.markdown(f"### 📍 Business Locations in {state_code or 'Selected Region'}")
    
    # Capture map state
    map_data = st_folium(m, width=800, height=500, returned_objects=["last_object_clicked", "center", "zoom"])

    # Return the current map center and zoom
    new_center = tuple(map_data["center"]) if map_data.get("center") else map_center
    new_zoom = map_data["zoom"] if map_data.get("zoom") else zoom

    return map_data, new_center, new_zoom
