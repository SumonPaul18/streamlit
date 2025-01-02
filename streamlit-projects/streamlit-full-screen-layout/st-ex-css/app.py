import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Load external CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("style.css")

# HTML for navigation bar
st.markdown(
    """
    <nav>
        <div class="nav-wrapper">
            <a href="#" class="navbar-logo">
                <img src="https://via.placeholder.com/50" alt="Logo" style="height: 50px; padding: 5px;">
            </a>
            <ul class="navbar-menu">
                <li><a href="#">Products</a></li>
                <li><a href="#">Solutions</a></li>
                <li><a href="#">Pricing</a></li>
                <li class="navbar-search">
                    <input type="text" placeholder="Search...">
                </li>
                <li><a href="#" class="navbar-signin">Sign In</a></li>
            </ul>
        </div>
    </nav>
    """,
    unsafe_allow_html=True
)

# Your Streamlit code here
st.markdown('<div class="content">', unsafe_allow_html=True)
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout with a responsive navigation bar using external CSS in Streamlit.")
st.markdown('</div>', unsafe_allow_html=True)