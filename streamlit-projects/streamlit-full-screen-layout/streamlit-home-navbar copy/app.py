import streamlit as st
from streamlit import container

# Set wide layout
st.set_page_config(layout="wide")

# Function to load files
def load_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Load the HTML and CSS files
navbar_html = load_file("navbar.html")
css_styles = load_file("styles.css")
sidebar_html = load_file("sidebar.html")
hero_html = load_file("hero.html")

# Apply custom CSS
st.markdown(f"<style>{css_styles}</style>", unsafe_allow_html=True)

# Display the navigation bar
st.markdown(navbar_html, unsafe_allow_html=True)

st.markdown(hero_html, unsafe_allow_html=True)
