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

# Sidebar content with circular rotating text around static centered text
st.sidebar.markdown("""
    <div id="container">
    <div id="circle">
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 150 150" width="150" height="150" xml:space="preserve">
            <defs>
                <path id="circlePath" d="M 75, 75 m -60, 0 a 60,60 0 0,1 120,0 a 60,60 0 0,1 -120,0 "/>
            </defs>
            <g>
                <use xlink:href="#circlePath" fill="none"/>
                <text fill="var(--text-black-900)">
                    <textPath xlink:href="#circlePath">Web Designer & Developer • Web Designer & Developer • Web Designer & Developer •</textPath>
                </text>
            </g>
        </svg>
        <a href="index.html">
            <div id="rk">R.K <hr class="rkhr"> Prajapati </div>
        </a>
    </div>
</div>

""", unsafe_allow_html=True)

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
