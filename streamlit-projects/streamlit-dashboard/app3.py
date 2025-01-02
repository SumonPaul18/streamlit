import streamlit as st

# Set page config for layout
st.set_page_config(page_title="My Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .nav {
        background-color: #f8f9fa;
        padding: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .sidebar {
        background-color: #f1f1f1;
        padding: 10px;
    }
    .profile {
        border-radius: 50%;
        width: 40px;
        height: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown('<div class="nav">', unsafe_allow_html=True)
st.markdown('<img src="your_logo_url" alt="Logo" style="height:40px;">', unsafe_allow_html=True)
st.text_input("Search...", placeholder="Search here...")
st.markdown('<img src="your_profile_image_url" class="profile" alt="Profile Image" onclick="alert(\'User Settings\');">', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Menu")
    menu_item = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    
    if menu_item == "Option 1":
        st.subheader("Submenu 1")
        sub_option = st.selectbox("Select Sub-option", ["Sub-option A", "Sub-option B"])
    
    elif menu_item == "Option 2":
        st.subheader("Submenu 2")
    
    elif menu_item == "Option 3":
        st.subheader("Submenu 3")

# Main content area
st.title("Welcome to My Dashboard")
st.write("This is where your main content will go.")
