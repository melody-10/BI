import folium
import json
import streamlit as st
import requests
from streamlit_folium import st_folium

# Dictionary mapping state abbreviations to their respective GeoJSON filenames
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
    'AB': None  # Alberta, Canada – not in the US dataset
}

def show_state_map(state_code, df):
    """
    Render a Folium map for the selected state with business locations.

    Parameters:
    - state_code (str): Two-letter state abbreviation.
    - df (pd.DataFrame): Filtered DataFrame with 'latitude', 'longitude', and 'name'.
    """
    geojson_file = STATE_GEOJSON_MAP.get(state_code)

    if not geojson_file:
        st.warning(f"No GeoJSON boundary data available for {state_code}.")
        return None

    geojson_url = f"https://raw.githubusercontent.com/edavgaun/topojson/master/countries/us-states/{geojson_file}"

    try:
        response = requests.get(geojson_url)
        response.raise_for_status()
        geo_data = response.json()
    except requests.RequestException:
        st.warning(f"GeoJSON file for {state_code} not found at URL: {geojson_url}")
        return None

    if df.empty:
        st.warning("No data to display on the map.")
        return None

    lat_center = df['latitude'].mean()
    lon_center = df['longitude'].mean()

    m = folium.Map(location=[lat_center, lon_center], zoom_start=7)

    folium.GeoJson(
        geo_data,
        name="State Boundary",
        style_function=lambda x: {
            "color": "blue",
            "weight": 2,
            "fillOpacity": 0.05
        }
    ).add_to(m)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row.get("name", "Unnamed"),
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    st_folium(m, width=800, height=500)

    return m
