import folium
import streamlit as st
from streamlit_folium import st_folium

def show_business_map(df, state_code=None):
    """
    Show a map of business locations using latitude and longitude.

    Parameters:
    - df (pd.DataFrame): DataFrame containing 'latitude', 'longitude', and optionally 'name'.
    - state_code (str): Optional, used for display purposes.
    """

    if df.empty:
        st.warning("No businesses to display on the map.")
        return

    # Center the map based on the mean lat/lon
    lat_center = df["latitude"].mean()
    lon_center = df["longitude"].mean()

    # Initialize map
    m = folium.Map(location=[lat_center, lon_center], zoom_start=7)

    # Add business markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row.get("name", "Unnamed"),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    st.markdown(f"### 📍 Business Locations in {state_code or 'Selected Region'}")
    st_folium(m, width=800, height=500)
