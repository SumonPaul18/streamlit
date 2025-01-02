import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def load_component(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Load CSS styles
css_styles = load_file("styles.css")

# Apply custom CSS
st.markdown(f"<style>{css_styles}</style>", unsafe_allow_html=True)

st.markdown(load_component('frontend/bootstrap/navbar.html'), unsafe_allow_html=True)


st.markdown(load_component('frontend/bootstrap/sidebar.html'), unsafe_allow_html=True)



st.title("Streamlit App with Multiple CSS Frameworks")

# Create columns
col1, col2, col3, col4, col5 = st.columns(5)

# Load and display components
with col1:
    st.markdown(load_component('frontend/bootstrap/bootstrap_component.html'), unsafe_allow_html=True)

with col2:
    st.markdown(load_component('frontend/bulma/bulma_component.html'), unsafe_allow_html=True)

with col3:
    st.markdown(load_component('frontend/materialize/materialize_component.html'), unsafe_allow_html=True)

with col4:
    st.markdown(load_component('frontend/semantic_ui/semantic_ui_component.html'), unsafe_allow_html=True)

with col5:
    st.markdown(load_component('frontend/foundation/foundation_component.html'), unsafe_allow_html=True)