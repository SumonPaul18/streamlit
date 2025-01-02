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

# Add custom CSS to ensure full width and height
full_width_css = f"""
<style>
    .full-width {{
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
    }}
</style>
<div class="full-width">
    {html_content}
</div>
"""

components.html(full_width_css, height=800, scrolling=True)