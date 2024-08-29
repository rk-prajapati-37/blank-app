import streamlit as st
from templates.home import show_home
from templates.about import show_about
from templates.contact import show_contact
import os

# Page layout settings - This should be at the top of your script
st.set_page_config(page_title="Home Page", layout="wide")

# Function to load custom CSS
def load_css():
    css_path = "assets/main.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.error("CSS file not found.")

# Load custom CSS
load_css()

# Sidebar Load Image
st.sidebar.image('data/logo/logo.png', width=100)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Display the selected page
if page == "Home":
    show_home()

elif page == "About":
    show_about()

elif page == "Contact":
    show_contact()
