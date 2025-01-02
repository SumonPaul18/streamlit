import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

def load_css(file_path):
    with open(file_path, 'r') as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def load_html(file_path):
    with open(file_path, 'r') as file:
        return file.read()

load_css('style.css')

# Load and display the main HTML file
html_content = load_html('index.html')
st.markdown(html_content, unsafe_allow_html=True)

# Add a button to load the about page
if st.button('About Us'):
    about_content = load_html('about.html')
    st.markdown(about_content, unsafe_allow_html=True)

st.title("My Streamlit App")
st.write("This is a Streamlit app with a Bootstrap navigation bar.")