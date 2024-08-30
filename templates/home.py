import streamlit as st

# Page content
def show_home():
    # Create two columns
    col1, col2 = st.columns(2)

    # Left Column - Title, Description, Text, Button
    with col1:
        st.markdown('<p class="sub-heading-txt">Hello!</p>', unsafe_allow_html=True)
        st.markdown('<p class="custom-title">I am Rohit Prajapati</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="designation-txt">( Web Designer & Developer )</h1>', unsafe_allow_html=True)
        st.markdown('<p class="custom-description">a passionate and seasoned web developer who holds a BSc in Computer Science from Mumbai University. With a focus on creating clean, responsive, and user-friendly websites, I bring a wealth of experience and expertise in WordPress, HTML, CSS, PHP, and JavaScript.</p>', unsafe_allow_html=True)
        st.markdown('<h4 class="designation-txt">Freelance Availability:</h4>', unsafe_allow_html=True)
        st.markdown('<p class="custom-description">Having had the privilege of contributing to reputable organizations, I am now excited to extend my services as a freelance web developer. My career has been shaped by a commitment to delivering high-quality, customized solutions.</p>', unsafe_allow_html=True)

        # Custom button using HTML
        st.markdown('<a href="#about" class="custom-button link-item outer-shadow hover-in-shadow">More about Me</a>', unsafe_allow_html=True)

    # Right Column - Profile Image with a surrounding div
    with col2:
        st.markdown(
            """
            <div class="image-container outer-shadow">
                <img src="https://raw.githubusercontent.com/rk-prajapati-37/blank-app/main/data/home_img/profile-pic.png" class="custom-image inner-shadow " alt="Profile Image">

            </div>
            """,
            unsafe_allow_html=True
        )


