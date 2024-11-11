import streamlit as st
import heart
import dibetic

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background-image: url('https://img.freepik.com/free-vector/medical-healthcare-blue-color_1017-26807.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .main {
        background-color: rgba(240, 242, 246, 0.85);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 60px;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: 2px solid #3498db;
        padding: 10px 20px;
        transition: all 0.3s ease;
        width: 100%;
        margin-bottom: 10px;
    }
    .stButton > button:hover {
        background-color: white;
        color: #3498db;
        border-color: #3498db;
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(52, 152, 219, 0.5);
    }
    .app-header {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 30px;
    }
    .app-description {
        text-align: center;
        color: #34495e;
        margin-bottom: 30px;
    }
    .heart-attack-bg {
        background-image: url('https://thumbs.dreamstime.com/b/blood-red-medical-background-28131836.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(240, 242, 246, 0.85);
        padding: 10px;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.1);
    }
    .sidebar-video {
        width: 100%;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to navigate to a specific page
def navigate_to(page):
    st.session_state.page = page

# Sidebar content
def sidebar_content():
    st.sidebar.markdown("""
    <video class="sidebar-video" src="https://cdnl.iconscout.com/lottie/premium/preview-watermark/programmer-is-coding-in-css-and-html-code-animation-download-lottie-json-gif-static-svg-file-formats--programming-lines-of-software-tester-pack-design-development-animations-9930744.mp4" autoplay="autoplay" muted="muted" loop="loop" playsinline="" type="video/mp4"></video>
    """, unsafe_allow_html=True)
    st.sidebar.title("About")
    st.sidebar.info("This app provides health predictions for heart attack and diabetes risks.")

# Home page
def home():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='app-header'>Health Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<p class='app-description'>Welcome to the Health Prediction App. Choose a prediction tool below:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Heart Attack Risk Prediction"):
            navigate_to('heart_attack')
    
    with col2:
        if st.button("Diabetes Risk Prediction"):
            navigate_to('diabetes')
    
    st.markdown("</div>", unsafe_allow_html=True)

# Main app logic
def main():
    sidebar_content()

    if st.session_state.page == 'home':
        home()
    elif st.session_state.page == 'heart_attack':
        st.markdown("<div class='heart-attack-bg'>", unsafe_allow_html=True)
        st.markdown("<div class='main'>", unsafe_allow_html=True)
        st.button("Back to Home", on_click=navigate_to, args=('home',))
        heart.main()
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif st.session_state.page == 'diabetes':
        st.markdown("<div class='main'>", unsafe_allow_html=True)
        st.button("Back to Home", on_click=navigate_to, args=('home',))
        dibetic.main()
        st.markdown("</div>", unsafe_allow_html=True)

    # Add a footer
    st.markdown("""
    <div class='footer'>
        <p style='margin: 0; font-size: 12px;'>© 2023 Health Prediction App. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()