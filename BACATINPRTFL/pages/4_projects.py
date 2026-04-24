import streamlit as st
# ... [Burger Button & Sidebar Code] ...


# 1. Initialize/Sync Sidebar State
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "collapsed"

st.set_page_config(layout="wide", initial_sidebar_state=st.session_state.sidebar_state)

# 2. Universal Hazard CSS (Matching your app.py design)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFD700; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #FFD700 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #FFD700 !important; text-shadow: 0 0 5px #FFD700;
    }
    [data-testid="stPageLink-NavLink"] {
        background-color: #1a1a1a !important; border: 1px solid #FFD700 !important;
        color: #FFD700 !important; border-radius: 0px !important; margin-bottom: 5px;
    }
    [data-testid="stPageLink-NavLink"]:hover { background-color: #FFD700 !important; color: #000000 !important; }
    div.stButton > button {
        background-color: #1a1a1a; color: #FFD700; border: 2px solid #FFD700; border-radius: 0px; width: 100%;
    }
    div.stButton > button:hover { background-color: #FFD700; color: #000000; }
    </style>
    """, unsafe_allow_html=True)


# 4. The Unified Sidebar Menu
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-top: -50px;'>SYSTEM MENU</h2>", unsafe_allow_html=True)
    st.write("---")
    st.page_link("app.py", label="CORE DASHBOARD", icon="☢️")
    st.page_link("pages/1_Home.py", label="HOME", icon="📟")
    st.page_link("pages/2_About.py", label="IDENTITY", icon="👤")
    st.page_link("pages/3_Skills.py", label="TECH-STACK", icon="⚡")
    st.page_link("pages/4_projects.py", label="MODULES", icon="📂")
    st.page_link("pages/5_Contacts.py", label="UPLINK", icon="📡")
    st.write("---")

# 5. --- DESIGNATED PAGE CONTENT STARTS HERE ---
st.markdown("## 📂 ACTIVE MODULES")

with st.container():
    st.markdown("""
    <div style="border: 2px solid #FFD700; padding: 25px; background-color: #1a1a1a;">
        <h2 style="color: #FFD700;">PROJECT T.R.A.C.E.</h2>
        <p><i>Integrated Barangay Management System with QR-Based Identification</i></p>
        <hr>
        <ul>
            <li><b>QR Identification Gateway:</b> Contactless resident verification.</li>
            <li><b>Automated Records:</b> Efficient resident data management.</li>
            <li><b>Direct Issuance:</b> Rapid generation of certificates/permits.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)