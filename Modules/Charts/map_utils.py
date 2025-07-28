import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd

def show_business_map(df, state_code=None):
    """
    Show a map of business locations using latitude and longitude.
    """

    if df.empty:
        st.warning("No businesses to display on the map.")
        return

    lat_center = df["latitude"].mean()
    lon_center = df["longitude"].mean()

    m = folium.Map(location=[lat_center, lon_center], zoom_start=7)

    for _, row in df.iterrows():
        lat = row.get("latitude")
        lon = row.get("longitude")

        if pd.notna(lat) and pd.notna(lon):
            folium.Marker(
                location=[lat, lon],
                popup=row.get("name", "Unnamed"),
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(m)

    st.markdown(f"### 📍 Business Locations in {state_code or 'Selected Region'}")
    st_folium(m, width=800, height=500, returned_objects=[])
