import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Custom CSS for full screen layout
st.markdown(
    """
    <style>
    .st-emotion-cache-1jicfl2 {
    width: 100%;
    padding: 6rem 1rem 10rem;
    min-width: auto;
    max-width: initial;
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