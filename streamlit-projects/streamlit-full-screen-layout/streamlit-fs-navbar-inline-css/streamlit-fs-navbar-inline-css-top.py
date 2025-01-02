import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Custom CSS for full screen layout and navigation bar
st.markdown(
    """
    <style>
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 0;
        min-width: auto;
        max-width: initial;
    }
    header, footer {
        visibility: hidden;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #4CAF50;
        padding: 0;
        margin: 0;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
    }
    .navbar-logo {
        font-size: 1.5rem;
        color: white;
        text-decoration: none;
        padding: 1rem;
    }
    .navbar-menu {
        display: flex;
        gap: 1rem;
    }
    .navbar-menu a {
        color: white;
        text-decoration: none;
        padding: 1rem;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .navbar-menu a:hover {
        background-color: #45a049;
    }
    .navbar-search {
        flex-grow: 1;
        margin: 0 1rem;
    }
    .navbar-search input {
        width: 100%;
        padding: 0.5rem;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .navbar-signin {
        background-color: #f44336;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        text-decoration: none;
        transition: background-color 0.3s;
    }
    .navbar-signin:hover {
        background-color: #e53935;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for navigation bar
st.markdown(
    """
    <div class="navbar">
        <img src="static/images/pc.png" class="navbar-logo">Logo</a>
        <div class="navbar-menu">
            <a href="#">Products</a>
            <a href="#">Solutions</a>
            <a href="#">Pricing</a>
        </div>
        <div class="navbar-search">
            <input type="text" placeholder="Search...">
        </div>
        <a href="#" class="navbar-signin">Sign In</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Your Streamlit code here
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout with a responsive navigation bar using Streamlit.")