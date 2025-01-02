import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import base64

# Page configuration
st.set_page_config(page_title="Dashboard", layout="wide")

# Custom CSS
st.markdown("""
<style>
    /* Main navigation bar styling */
    .navbar {
        padding: 1rem;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
    .sidebar {
        padding: 20px;
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
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Navigation bar
def create_navbar():
    navbar_html = """
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <div class="d-flex align-items-center">
                <img src="https://via.placeholder.com/40" class="logo-img" alt="Logo">
                <button class="btn btn-link" onclick="toggleSidebar()">
                    <i class="fas fa-bars"></i>
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

# Sidebar menu
def create_sidebar():
    with st.sidebar:
        menu = option_menu(
            "Main Menu",
            ["Dashboard", "Analytics", "Reports", "Settings"],
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
        if menu == "Analytics":
            st.sidebar.markdown("### Analytics Options")
            st.sidebar.checkbox("Sales Analytics")
            st.sidebar.checkbox("User Analytics")
            st.sidebar.checkbox("Product Analytics")
        
        elif menu == "Reports":
            st.sidebar.markdown("### Report Types")
            st.sidebar.radio("Select Report", 
                           ["Daily Report", "Weekly Report", "Monthly Report"])

# Required JavaScript for sidebar toggle
js = """
<script>
function toggleSidebar() {
    const sidebar = document.querySelector('[data-testid="stSidebar"]');
    if (sidebar) {
        const isVisible = sidebar.style.width !== '0px';
        sidebar.style.width = isVisible ? '0px' : '250px';
        sidebar.style.visibility = isVisible ? 'hidden' : 'visible';
    }
}
</script>

<!-- Font Awesome for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<!-- Bootstrap CSS and JS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
"""

# Main application
def main():
    # Inject custom JS and CSS
    st.markdown(js, unsafe_allow_html=True)
    
    # Create navigation bar
    create_navbar()
    
    # Create sidebar
    create_sidebar()
    
    # Main content area
    st.title("Welcome to Dashboard")
    
    # Add your dashboard content here with custom metric cards
    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Total Users", "1,234")
    with col2:
        metric_card("Active Users", "789")
    with col3:
        metric_card("Revenue", "$50,000")

if __name__ == "__main__":
    main()