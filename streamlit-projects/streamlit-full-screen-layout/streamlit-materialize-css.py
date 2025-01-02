import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Materialize CSS
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# HTML for navigation bar
st.markdown(
    """
    <nav>
        <div class="nav-wrapper">
            <a href="#" class="brand-logo">
                <img src="https://via.placeholder.com/50" alt="Logo" style="height: 50px; padding: 5px;">
            </a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li><a href="#">Products</a></li>
                <li><a href="#">Solutions</a></li>
                <li><a href="#">Pricing</a></li>
                <li>
                    <form>
                        <div class="input-field">
                            <input id="search" type="search" required>
                            <label class="label-icon" for="search"><i class="material-icons">search</i></label>
                            <i class="material-icons">close</i>
                        </div>
                    </form>
                </li>
                <li><a href="#" class="btn">Sign In</a></li>
            </ul>
        </div>
    </nav>
    """,
    unsafe_allow_html=True
)

# Materialize JS
st.markdown(
    """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    """,
    unsafe_allow_html=True
)

# Your Streamlit code here
st.markdown('<div style="padding-top: 4rem;">', unsafe_allow_html=True)
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout with a responsive navigation bar using Materialize CSS in Streamlit.")
st.markdown('</div>', unsafe_allow_html=True)