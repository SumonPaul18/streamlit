import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Custom CSS for full screen layout
st.markdown(
    """
    <style>
    .main .block-container {
        padding: 0;
        margin: 0;
        max-width: 100%;
    }
    header, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit code here
st.title("Full Screen Layout Example")
st.write("This is an example of a full screen layout using Streamlit.")