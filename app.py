import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set up the app title
st.title("Anime Wallpaper App")

# Function to fetch images from the API
def fetch_images():
    url = "https://api.waifu.pics/sfw/waifu"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "url" in data:
                return [data["url"]]
        return []
    except Exception as e:
        st.error(f"Error fetching images: {e}")
        return []

# State to store fetched images
if "image_list" not in st.session_state:
    st.session_state.image_list = []

# Button to refresh images
if st.button("Refresh Wallpapers"):
    st.session_state.image_list = fetch_images()

# Display loading message while images are being fetched
if not st.session_state.image_list:
    st.write("No images available. Click 'Refresh Wallpapers' to fetch.")
else:
    st.write("### Anime Wallpapers")
    cols = st.columns(3)
    for index, image_url in enumerate(st.session_state.image_list):
        with cols[index % 3]:
            # Display the image as a thumbnail
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                if st.button("View Fullscreen", key=index):
                    st.image(image, use_column_width=True, caption="Anime Wallpaper")
                else:
                    st.image(image, use_column_width=True)
            else:
                st.error("Failed to load image.")