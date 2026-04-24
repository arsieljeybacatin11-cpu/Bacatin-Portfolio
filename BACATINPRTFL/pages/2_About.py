import os
import streamlit as st

# --- 1. CORE SYSTEM CSS & NAVIGATION ---
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "collapsed"

st.set_page_config(page_title="ARSIEL | IDENTITY", layout="wide", initial_sidebar_state=st.session_state.sidebar_state)

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFD700; font-family: 'Courier New', monospace; }
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #FFD700 !important; }
    .achievement-card {
        border: 1px solid #FFD700;
        padding: 10px;
        background-color: #1a1a1a;
        text-align: center;
    }
    .mission-box {
        border: 2px solid #FFD700;
        padding: 30px;
        background-color: #0a0a0a;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>SYSTEM MENU</h2>", unsafe_allow_html=True)
    st.page_link("app.py", label="CORE DASHBOARD", icon="☢️")
    st.page_link("pages/1_Home.py", label="HOME", icon="📟")
    st.page_link("pages/2_About.py", label="IDENTITY", icon="👤")
    st.page_link("pages/3_Skills.py", label="TECH-STACK", icon="⚡")
    st.page_link("pages/4_projects.py", label="MODULES", icon="📂")
    st.page_link("pages/5_Contacts.py", label="UPLINK", icon="📡")

# --- 2. MISSION OBJECTIVE QUOTE ---
st.markdown("""
<div class="mission-box">
    <p style="background-color: #FFD700; color: #000000; display: inline-block; padding: 2px 10px; font-weight: bold;">MISSION OBJECTIVE</p>
    <h2 style="color: #FFD700; text-transform: uppercase;">
        "To leverage automation and data visualization to solve real-world community problems through Ideas."
    </h2>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🏆 SYSTEM ACHIEVEMENTS")

# This path works on Live Streamlit Cloud and Local VS Code
# Make sure these 4 files are physically inside your 'pages' folder!
achievement_links = [
    "pages/cert1.png.jpg", 
    "pages/cert2.png.jpg", 
    "pages/cert3.png.jpg", 
    "pages/cert4.png.jpg"
]

cols = st.columns(4)
for i, col in enumerate(cols):
    with col:
        # Get the filename for the specific column
        img_path = achievement_links[i]
        
        # Check if file exists to prevent the app from crashing
        if os.path.exists(img_path):
            st.markdown('<div class="achievement-card">', unsafe_allow_html=True)
            st.image(img_path, caption=f"DATA_LOG_{i+1}", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # If it's not in /pages, it checks the root folder as a backup
            backup_path = img_path.replace("pages/", "")
            if os.path.exists(backup_path):
                st.markdown('<div class="achievement-card">', unsafe_allow_html=True)
                st.image(backup_path, caption=f"DATA_LOG_{i+1}", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning(f"FILE NOT FOUND: {img_path}")
