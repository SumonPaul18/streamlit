import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .navbar {
        background-color: #333;
        overflow: hidden;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 1000;
    }
    .navbar a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    .navbar .logo {
        float: left;
        font-size: 24px;
        font-weight: bold;
    }
    .navbar .right {
        float: right;
    }
    .sidebar {
        height: 100%;
        width: 0;
        position: fixed;
        top: 50px;
        left: 0;
        background-color: #111;
        overflow-x: hidden;
        transition: 0.5s;
        padding-top: 60px;
    }
    .sidebar a {
        padding: 8px 8px 8px 32px;
        text-decoration: none;
        font-size: 25px;
        color: #818181;
        display: block;
        transition: 0.3s;
    }
    .sidebar a:hover {
        color: #f1f1f1;
    }
    .sidebar .closebtn {
        position: absolute;
        top: 0;
        right: 25px;
        font-size: 36px;
        margin-left: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
    <div class="navbar">
        <a href="#home" class="logo">Company Logo</a>
        <a href="#item1">Item 1</a>
        <a href="#item2">Item 2</a>
        <a href="#item3">Item 3</a>
        <a href="#signin" class="right">Sign In</a>
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.markdown("""
    <div id="mySidebar" class="sidebar">
        <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×</a>
        <a href="#">Link 1</a>
        <a href="#">Link 2</a>
        <a href="#">Link 3</a>
    </div>
    <div id="main">
        <button class="openbtn" onclick="openNav()">☰ Open Sidebar</button>  
    </div>
    <script>
    function openNav() {
        document.getElementById("mySidebar").style.width = "250px";
    }
    function closeNav() {
        document.getElementById("mySidebar").style.width = "0";
    }
    </script>
""", unsafe_allow_html=True)

# Main content
st.write("Main content goes here...")