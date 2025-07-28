import folium
import streamlit as st
import requests
import json
from streamlit_folium import st_folium

# Your dictionary: 11 U.S. states + Alberta (AB)
STATE_GEOJSON_MAP = {
    'AZ': 'AZ-04-arizona-counties.json',
    'CA': 'CA-06-california-counties.json',
    'FL': 'FL-12-florida-counties.json',
    'IN': 'IN-18-indiana-counties.json',
    'LA': 'LA-22-louisiana-parishes.json',
    'MO': 'MO-29-missouri-counties.json',
    'NJ': 'NJ-34-new-jersey-counties.json',
    'NV': 'NV-32-nevada-counties.json',
    'PA': 'PA-42-pennsylvania-counties.json',
    'TN': 'TN-47-tennessee-counties.json',
    'AB': None  # Alberta – no GeoJSON
}

def show_state_map(state_code, df):
    """
    Render a Folium map for the selected state with business locations.
    """

    geojson_file = STATE_GEOJSON_MAP.get(state_code)

    if not geojson_file:
        st.warning(f"No GeoJSON boundary data available for `{state_code}`.")
        return

    # Construct URL from your GitHub repo
    url = f"https://raw.githubusercontent.com/edavgaun/topojson/master/countries/us-states/{geojson_file}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        geo_data = response.json()
    except Exception as e:
        st.error(f"Error loading GeoJSON for `{state_code}`: {e}")
        return

    if df.empty:
        st.warning("No business data to map.")
        return

    lat_center = df["latitude"].mean()
    lon_center = df["longitude"].mean()

    m = folium.Map(location=[lat_center, lon_center], zoom_start=7)

    # Add the state boundary
    folium.GeoJson(
        geo_data,
        name="Boundary",
        style_function=lambda x: {
            "color": "blue",
            "weight": 2,
            "fillOpacity": 0.05
        }
    ).add_to(m)

    # Add business markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row.get("name", "Unnamed"),
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    # Render in Streamlit
    st_folium(m, width=800, height=500)
