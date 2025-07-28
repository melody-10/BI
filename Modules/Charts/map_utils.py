import folium
import json
import streamlit as st

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
    """
    geojson_file = STATE_GEOJSON_MAP.get(state_code)

    if not geojson_file:
        st.warning(f"No GeoJSON boundary data available for {state_code}.")
        return None

    geojson_path = f"topojson/countries/us-states/{geojson_file}"
    try:
        with open(geojson_path, "r") as f:
            geo_data = json.load(f)
    except FileNotFoundError:
        st.warning(f"GeoJSON file for {state_code} not found at path: {geojson_path}")
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

    return m
