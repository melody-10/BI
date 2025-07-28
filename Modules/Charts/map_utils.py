import folium
import json
import streamlit as st

def show_state_map(state_code, df):
    """
    Render a Folium map for the selected state with business locations.

    Parameters:
    - state_code (str): Two-letter state abbreviation.
    - df (pd.DataFrame): Filtered DataFrame with 'latitude', 'longitude', and 'name'.
    """
    # Load the GeoJSON file for the state
    geojson_path = f"countries/us-states/{state_code}.geojson"
    try:
        with open(geojson_path, "r") as f:
            geo_data = json.load(f)
    except FileNotFoundError:
        st.warning(f"GeoJSON for {state_code} not found.")
        return None

    # Center map around the average location of filtered businesses
    if df.empty:
        st.warning("No data to display on the map.")
        return None

    lat_center = df['latitude'].mean()
    lon_center = df['longitude'].mean()

    m = folium.Map(location=[lat_center, lon_center], zoom_start=7)

    # Add state boundary
    folium.GeoJson(
        geo_data,
        name="State Boundary",
        style_function=lambda x: {
            "color": "blue",
            "weight": 2,
            "fillOpacity": 0.05
        }
    ).add_to(m)

    # Add markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row.get("name", "Unnamed"),
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    return m
