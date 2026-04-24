import streamlit as st

import time

# --- INITIALIZATION LOGIC ---
if "initialized" not in st.session_state:
    # This creates a full-screen black overlay for the loading sequence
    loading_placeholder = st.empty()
    
    with loading_placeholder.container():
        st.markdown("""
            <style>
            .loading-text {
                color: #FFD700;
                font-family: 'Courier New', monospace;
                text-align: center;
                margin-top: 20%;
                text-shadow: 0 0 10px #FFD700;
            }
            </style>
            <div class="loading-text">
                <h1>CORE SYSTEM INITIALIZING...</h1>
                <p>ACCESSING ARSIEL_DATA_VOL_01</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Progress bar styled to match your theme
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)  # Adjust speed here (0.02 is about 2 seconds)
            progress_bar.progress(percent_complete + 1)
            
        st.success("INITIALIZATION COMPLETE")
        time.sleep(0.5)
    
    # Clear the loading screen and set state so it doesn't repeat on every click
    loading_placeholder.empty()
    st.session_state.initialized = True

if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "collapsed"

st.set_page_config(page_title="ARSIEL | CORE", layout="wide", initial_sidebar_state=st.session_state.sidebar_state)

# Shared Hazard CSS + SIDEBAR ENHANCEMENTS
st.markdown("""
    <style>
    /* Main App Background */
    .stApp { background-color: #000000; color: #FFD700; font-family: 'Courier New', monospace; }
    
    /* Sidebar Container Design */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 2px solid #FFD700 !important;
    }
    
    /* Hide default navigation links */
    [data-testid="stSidebarNav"] {display: none;}

    /* Sidebar Titles and Text */
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #FFD700 !important;
        text-shadow: 0 0 5px #FFD700;
    }

    /* Custom Page Link Design (Hazard Buttons) */
    [data-testid="stPageLink-NavLink"] {
        background-color: #1a1a1a !important;
        border: 1px solid #FFD700 !important;
        color: #FFD700 !important;
        border-radius: 0px !important;
        margin-bottom: 5px;
        transition: 0.3s;
    }
    
    [data-testid="stPageLink-NavLink"]:hover {
        background-color: #FFD700 !important;
        color: #000000 !important;
    }

    /* Global Button Style */
    div.stButton > button {
        background-color: #1a1a1a; color: #FFD700; border: 2px solid #FFD700; border-radius: 0px; width: 100%;
    }
    div.stButton > button:hover { background-color: #FFD700; color: #000000; }
    
    .hazard-header { text-align: center; color: #FFD700; border: 2px solid #FFD700; padding: 20px; text-shadow: 0 0 10px #FFD700; }
    </style>
    """, unsafe_allow_html=True)



# The Unified Sidebar Menu
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-top: -50px;'>SYSTEM MENU</h2>", unsafe_allow_html=True)
    st.write("---")
    # All links now inherit the CSS styling defined above
    st.page_link("app.py", label="CORE DASHBOARD", icon="☢️")
    st.page_link("pages/1_Home.py", label="HOME", icon="📟")
    st.page_link("pages/2_About.py", label="IDENTITY", icon="👤")
    st.page_link("pages/3_Skills.py", label="TECH-STACK", icon="⚡")
    st.page_link("pages/4_projects.py", label="MODULES", icon="📂")
    st.page_link("pages/5_Contacts.py", label="UPLINK", icon="📡")
    st.write("---")
    st.markdown("<p style='font-size: 10px; text-align: center;'>ENCRYPTION LEVEL: ARSIEL-X</p>", unsafe_allow_html=True)

# Splash Content
st.markdown("<div class='hazard-header'><h1>☢️ CORE SYSTEM INITIALIZED: ARSIEL ☢️</h1><p>VERIFYING CREDENTIALS... ACCESS GRANTED</p></div>", unsafe_allow_html=True)
st.write("")
