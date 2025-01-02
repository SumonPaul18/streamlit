import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(page_title="Dashboard", layout="wide")

# Custom CSS
st.markdown("""
<style>
    /* Reset padding and margin for the main container */
    .main {
        padding-top: 0 !important;
    }
    
    [data-testid="stAppViewContainer"] {
        padding-top: 0;
    }
    
    [data-testid="stHeader"] {
        display: none;
    }
    
    /* Main navigation bar styling */
    .navbar {
        position: relative;
        padding: 1rem;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0;
        width: 100%;
    }
    
    /* Logo styling */
    .logo-img {
        height: 40px;
        margin-right: 15px;
    }
    
    /* Search bar styling */
    .search-bar {
        max-width: 400px;
        margin: 0 auto;
    }
    
    /* Profile image styling */
    .profile-img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        cursor: pointer;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 3.5rem;
    }
    
    /* Ensure sidebar appears below navbar */
    [data-testid="stSidebar"] {
        padding-top: 3.5rem;
        z-index: 1;
    }
    
    /* Custom menu styling */
    .nav-link {
        color: #333;
        padding: 10px 15px;
    }
    
    .nav-link:hover {
        background: #f8f9fa;
    }
    
    /* Custom card styling */
    .metric-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    
    .metric-card h3 {
        color: #333;
        font-size: 16px;
        margin-bottom: 10px;
    }
    
    .metric-card p {
        color: #02ab21;
        font-size: 24px;
        font-weight: bold;
        margin: 0;
    }
    
    /* Hide default streamlit components */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Navigation bar
def create_navbar():
    navbar_html = """
    <nav class="navbar">
        <div class="container-fluid">
            <div class="d-flex align-items-center">
                <img src="https://via.placeholder.com/40" class="logo-img" alt="Logo">
                <button class="btn" onclick="window.Streamlit.setComponentValue(true)">
                    <i class="fas fa-chevron-right"></i>
                </button>
            </div>
            <div class="search-bar">
                <input type="text" class="form-control" placeholder="Search...">
            </div>
            <div class="dropdown">
                <img src="https://via.placeholder.com/40" class="profile-img" 
                     data-bs-toggle="dropdown" alt="Profile">
                <ul class="dropdown-menu dropdown-menu-end">
                    <li><a class="dropdown-item" href="#">Profile</a></li>
                    <li><a class="dropdown-item" href="#">Settings</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Logout</a></li>
                </ul>
            </div>
        </div>
    </nav>
    """
    st.markdown(navbar_html, unsafe_allow_html=True)

# Custom metric card
def metric_card(title, value):
    st.markdown(f"""
        <div class="metric-card">
            <h3>{title}</h3>
            <p>{value}</p>
        </div>
    """, unsafe_allow_html=True)

# Sidebar content
def sidebar_content():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Dashboard", "Analytics", "Reports", "Settings"],
            icons=['house', 'graph-up', 'file-text', 'gear'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
        
        # Submenu based on selection
        if selected == "Analytics":
            st.markdown("### Analytics Options")
            st.checkbox("Sales Analytics")
            st.checkbox("User Analytics")
            st.checkbox("Product Analytics")
        
        elif selected == "Reports":
            st.markdown("### Report Types")
            st.radio("Select Report", 
                    ["Daily Report", "Weekly Report", "Monthly Report"])

        return selected

# Required JavaScript for icons and Bootstrap
js = """
<!-- Font Awesome for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<!-- Bootstrap CSS and JS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>

<script>
// Initialize the sidebar state
if (window.Streamlit) {
    window.Streamlit.setComponentValue(false);
}
</script>
"""

# Main application
def main():
    # Inject custom JS and CSS
    st.markdown(js, unsafe_allow_html=True)
    
    # Create navigation bar
    create_navbar()
    
    # Create sidebar content
    selected = sidebar_content()
    
    # Add some spacing after navbar
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    
    # Main content area
    if selected == "Dashboard":
        st.title("Welcome to Dashboard")
        
        # Add your dashboard content here with custom metric cards
        col1, col2, col3 = st.columns(3)
        with col1:
            metric_card("Total Users", "1,234")
        with col2:
            metric_card("Active Users", "789")
        with col3:
            metric_card("Revenue", "$50,000")
    
    elif selected == "Analytics":
        st.title("Analytics")
        # Add your analytics content here
    
    elif selected == "Reports":
        st.title("Reports")
        # Add your reports content here
    
    elif selected == "Settings":
        st.title("Settings")
        # Add your settings content here

if __name__ == "__main__":
    main()