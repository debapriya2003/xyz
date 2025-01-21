import streamlit as st
import requests
from PIL import Image
from io import BytesIO
API_URL = "https://api.nekosapi.com/v4/images/random"
def fetch_random_images(limit=6):
    try:
        params = {"limit": limit}
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                image_urls = [item['url'] for item in data['items']]
                return image_urls
            else:
                st.error("No images found in the response.")
                return None
        else:
            st.error(f"Failed to fetch images. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Failed to fetch images: {str(e)}")
        return None
def display_image_grid(image_urls):
    cols = st.columns(3)
    for i, image_url in enumerate(image_urls):
        col = cols[i % 3]  # Cycle through the columns
        with col:
            st.image(image_url, use_container_width=True)
# Main layout
def main():
    st.title("Anime Wallpaper Grid 🎨")
    st.markdown("Discover anime wallpapers!")
    # Inputs to control the number of images
    limit = st.slider("Select number of images", 1, 100, 6)
    # Fetch button to get random anime wallpapers
    if st.button("Fetch Random Wallpapers"):
        image_urls = fetch_random_images(limit=limit)
        if image_urls:
            display_image_grid(image_urls)
# Run the Streamlit app
if __name__ == "__main__":
    main()
