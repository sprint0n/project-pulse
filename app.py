import streamlit as st
import pandas as pd
import json
import os # Import the os module for file path operations

# --- Streamlit App Configuration and Layout ---

st.set_page_config(
    page_title="JSON Geolocation Tracker",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🗺️ JSON Geolocation Mapper (Auto-Load)")
st.markdown("This app automatically loads `location.json` from the same directory as the script.")
st.markdown("---")

# Define the expected local file path
FILE_PATH = 'location.json'
location_data = None

# 1. Automatic File Loading Logic
st.header(f"1. Loading data from **`{FILE_PATH}`**...")

try:
    # Check if the file exists and load it
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            location_data = json.load(f)
        st.success(f"Successfully loaded data from **{FILE_PATH}**.")
        st.markdown("---")
    else:
        st.error(f"File **`{FILE_PATH}`** not found in the application directory.")
        st.warning("Please place your `location.json` file next to `app.py`.")
        st.stop()
        
except FileNotFoundError:
    st.error(f"Error: The file '{FILE_PATH}' was not found.")
    st.stop()
except json.JSONDecodeError:
    st.error(f"Error: The content of '{FILE_PATH}' is not a valid JSON format. Please check the file's contents.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()


# --- Display Location Details (Only if data was successfully loaded) ---
if location_data:
    
    # Extract key location data
    lat = location_data.get('latitude')
    lon = location_data.get('longitude')
    city = location_data.get('city')
    region = location_data.get('region')
    country = location_data.get('country_name')
    ip_address = location_data.get('ip', 'N/A (IP not in data)') # Safely handle missing 'ip' field
    postal_code = location_data.get('postal')

    # Check for essential data before proceeding
    if lat is None or lon is None or city is None:
        st.error("Error: Missing essential geographic data ('latitude', 'longitude', or 'city') in the JSON file.")
        st.stop()
        
    st.header(f"2. Location Details for {city}, {region}")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("IP Address (if present)", ip_address)
        st.metric("City / State", f"{city} / {region}")

    with col2:
        st.metric("Latitude", f"{lat}°")
        st.metric("Longitude", f"{lon}°")
        
    with col3:
        st.metric("Country", country)
        st.metric("Postal Code", postal_code)

    st.metric("Organization (ASN)", location_data.get('org', 'N/A'))
    st.metric("Timezone", location_data.get('timezone', 'N/A'))


    st.markdown("---")

    # 2. Prepare Data for st.map
    map_df = pd.DataFrame({
        'latitude': [lat],
        'longitude': [lon],
        'location_name': [f"{city}, {region}"]
    })

    st.header("3. Interactive Map View")
    st.info(f"The map pin marks the precise location: **{city}, {region}, {country}**.")

    # 3. Display the map
    # We use zoom=10 for a good, focused view of the city area.
    st.map(map_df, zoom=10)
    
    # 4. Optional: Show raw JSON data
    st.subheader("Raw Data Preview")
    st.json(location_data)

# Custom CSS for a better look
st.markdown("""
<style>
.stHeader, .stMetric, .stMetric label div {
    color: #4B0082; /* Indigo/Purple theme */
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


"""
Reflection:
I found the streamlit to be quite interesting. I won't pretend I could have done this myself, but I did manage to get a few things running myself. Extracting location data was pretty simple once I figured out
how to do it. AI helped me when I asked how I would create a dashboard to display data from a JSON file, and then how I would map a city location with given lat and long.





"""