import base64
import streamlit as st

@st.cache_data
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def build_markup_for_logo(
    png_file,
    background_position="50% 5%",  # Adjusted to position higher
    margin_top="0",
    image_width="60%",
    image_height="150px",  # Adjust as needed
):
    binary_string = get_base64_of_bin_file(png_file)
    return f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{binary_string}");
                background-repeat: no-repeat;
                background-position: {background_position};
                background-size: {image_width} {image_height};
                padding-top: 120px;  /* Adjust this value to control the space above the content */
                z-index: 1;          /* Ensure the sidebar content is above the background image */
            }}
            [data-testid="stSidebarNav"] .css-1d391kg {{
                position: relative;
                z-index: 2;  /* Ensure that the sidebar content is above the background image */
            }}
        </style>
    """
