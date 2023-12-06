import streamlit as st
import pandas as pd
import pydeck as pdk

# Streamlit application
def main():
    st.title("Interactive Globe Map App")

    # Obtain user input for latitude and longitude
    latitude = st.number_input("Please input Latitude:", min_value=-90.0, max_value=90.0, value=0.0)
    longitude = st.number_input("Please input Longitude:", min_value=-180.0, max_value=180.0, value=0.0)

    # Retrieve existing marker data from session state
    marker_data = st.session_state.marker_data if "marker_data" in st.session_state else pd.DataFrame()

    # Update marker data with the new input
    new_marker = pd.DataFrame({
        'latitude': [latitude],
        'longitude': [longitude],
        'tooltip': [f'Marker {len(marker_data) + 1}'],
    })
    marker_data = pd.concat([marker_data, new_marker], ignore_index=True)

    # Save the updated marker data to session state
    st.session_state.marker_data = marker_data

    # Render the globe map with all accumulated markers
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
            latitude=0.0,
            longitude=0.0,
            zoom=2,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=marker_data,
                get_position='[longitude, latitude]',
                get_color='[255, 0, 0, 255]',  # Red color for the markers
                get_radius=200000,
                pickable=True,
            ),
        ],
    ))

    # Display the current marker location
    st.write("Location of the Marker: Latitude {}, Longitude {}".format(latitude, longitude))

    # Add a clear button to reset the markers
    if st.button("Clear Markers"):
        # Clear the marker data in session state
        st.session_state.marker_data = pd.DataFrame()

if __name__ == "__main__":
    main()
