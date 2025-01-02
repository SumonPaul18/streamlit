import streamlit as st
from jinja2 import Environment, FileSystemLoader
import streamlit.components.v1 as components

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def render_template(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

st.set_page_config(layout="wide")  # Set the layout to wide

# Dynamic data
context = {
    "title": "My Streamlit App with Multiple CSS Frameworks"
}

# Load and display template
html_content = render_template('component.html', context)
components.html(html_content, height=600, scrolling=True)
#components.html(html_content, width=1000, height=800)