import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Load external HTML and CSS
with open("navbar.html", "r") as f:
    navbar_html = f.read()

st.markdown(navbar_html, unsafe_allow_html=True)

# Your Streamlit code here
st.markdown('<div style="padding-top: 4rem;">', unsafe_allow_html=True)
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout with a responsive navigation bar using Bootstrap in Streamlit.")
st.markdown('</div>', unsafe_allow_html=True)