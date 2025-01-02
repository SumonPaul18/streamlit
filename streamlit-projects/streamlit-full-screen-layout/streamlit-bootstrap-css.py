import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Bootstrap CSS
st.markdown(
    """
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# HTML for navigation bar
st.markdown(
    """
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        <a class="navbar-brand" href="#">
            <img src="https://via.placeholder.com/50" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
            Logo
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Products <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Solutions</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Pricing</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            </form>
            <a class="btn btn-outline-success my-2 my-sm-0" href="#">Sign In</a>
        </div>
    </nav>
    """,
    unsafe_allow_html=True
)

# Bootstrap JS and Popper.js
st.markdown(
    """
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    """,
    unsafe_allow_html=True
)

# Your Streamlit code here
st.markdown('<div style="padding-top: 4rem;">', unsafe_allow_html=True)
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout with a responsive navigation bar using Bootstrap in Streamlit.")
st.markdown('</div>', unsafe_allow_html=True)