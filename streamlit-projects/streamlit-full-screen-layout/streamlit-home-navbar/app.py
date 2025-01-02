import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Function to load files
def load_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Load the HTML and CSS files
navbar_html = load_file("navbar.html")
css_styles = load_file("styles.css")
navbar2_html = load_file("sidebar.html")
hero_html = load_file("hero.html")

# Apply custom CSS
st.markdown(f"<style>{css_styles}</style>", unsafe_allow_html=True)

# Display the navigation bar
st.markdown(navbar_html, unsafe_allow_html=True)

with st.container():
    
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.title("This is an a Container Example")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(navbar2_html, unsafe_allow_html=True) 
    with col2:
        st.markdown(hero_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.title("This is an a Columns Example")

col1, col2 = st.columns(2)
with col1:
    st.markdown(navbar2_html, unsafe_allow_html=True) 
with col2:
    st.markdown(hero_html, unsafe_allow_html=True)


st.title("This is an a Custom-Columns Example")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<div class="custom-padding">{navbar2_html}</div>', unsafe_allow_html=True)

with col2:
    st.markdown(hero_html, unsafe_allow_html=True)

#with st.container():
#    st.markdown(navbar2_html, unsafe_allow_html=True) 

# Create columns
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="custom-padding">', unsafe_allow_html=True)
        st.markdown(navbar2_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown(hero_html, unsafe_allow_html=True)

# Your Streamlit code here
st.markdown('<div class="content">', unsafe_allow_html=True)
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout with a responsive navigation bar using Streamlit.")
st.markdown('</div>', unsafe_allow_html=True)