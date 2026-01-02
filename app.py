import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="SmartCrowd OS | AI Safety Terminal",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional UI Styling
st.markdown("""
    <style>
    .main { background-color: #0b0d11; color: #e6edf3; }
    [data-testid="stMetricValue"] { font-family: 'Courier New', monospace; color: #00d4ff; }
    .stAlert { background-color: #161b22; border: 1px solid #30363d; }
    div[data-testid="stExpander"] { border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL STATE MANAGEMENT ---
if 'alerts' not in st.session_state:
    st.session_state.alerts = [
        {"time": "19:04:22", "msg": "System Calibration Complete", "type": "success"},
        {"time": "19:10:05", "msg": "Sensor Node 14 Active", "type": "info"}
    ]

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=70)
    st.title("Admin Terminal")
    st.caption("AI-Powered Public Safety Interface")
    
    nav = st.radio("Navigation", 
        ["Strategic Goals", "Live Command Center", "AI Analytics", "System Deployment"])
    
    st.divider()
    st.subheader("Infrastructure Status")
    st.status("AI Core: Operational", state="complete")
    st.write("🛰️ Satellite Link: **Stable**")
    st.write("📷 Camera Nodes: **1,240 Active**")

# --- 4. MODULE: STRATEGIC GOALS ---
if nav == "Strategic Goals":
    st.title("🛡️ SmartCrowd OS: Mission Protocol")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### Prevent\nAI detects early signs of 'crowd turbulence' before it turns into a crush.")
    with col2:
        st.info("### Protect\nReal-time GPS routing for emergency responders to avoid dense areas.")
    with col3:
        st.info("### Predict\nMachine Learning models forecast density for the next 30-60 minutes.")

    st.divider()
    
    left, right = st.columns(2)
    with left:
        st.error("#### The Safety Gap")
        st.write("""
        * **Latency:** Human guards take ~15 mins to report a surge.
        * **Blindspots:** CCTV blindspots lead to delayed rescues.
        * **Inefficiency:** Panic often spreads faster than instructions.
        """)
    with right:
        st.success("#### The SmartCrowd Solution")
        st.write("""
        * **Instant Alerts:** 0.5s detection via Edge AI processing.
        * **Total Visibility:** Sensor fusion combines CCTV + Wi-Fi Triangulation.
        * **Direct Comms:** Push-alerts sent directly to on-ground staff apps.
        """)

# --- 5. MODULE: LIVE COMMAND CENTER ---
elif nav == "Live Command Center":
    st.title("🛰️ Live Operational Intelligence")
    
    # Live KPI Row
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Live Attendance", "42,892", "+1.4%")
    k2.metric("Flow Velocity", "1.2 m/s", "Stable")
    k3.metric("Critical Points", "2 Areas", "-1", delta_color="inverse")
    k4.metric("Avg Response", "2.8 min", "Target Met")

    # Layout: Map & Alert Feed
    map_col, feed_col = st.columns([2, 1])
    
    with map_col:
        st.subheader("📍 Real-Time Density Heatmap")
        
        # Generating synthetic density data for a heatmap effect
        np.random.seed(42)
        lats = np.random.normal(40.7128, 0.01, 1500)
        lons = np.random.normal(-74.0060, 0.01, 1500)
        
        # Creating a Mapbox Density Heatmap
        fig_map = px.density_mapbox(
            lat=lats, 
            lon=lons, 
            radius=15,
            center=dict(lat=40.7128, lon=-74.0060), 
            zoom=13,
            mapbox_style="carto-darkmatter",
            color_continuous_scale="Jet" # Classic Thermal look: Blue (Cold) to Red (Hot)
        )
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#0b0d11")
        st.plotly_chart(fig_map, use_container_width=True)

    with feed_col:
        st.subheader("🔔 Incident Feed")
        if st.button("🚨 Simulate Critical Surge"):
            new_alert = {"time": datetime.now().strftime("%H:%M:%S"), "msg": "Density Spike: Gate 4", "type": "error"}
            st.session_state.alerts.insert(0, new_alert)
            
        for a in st.session_state.alerts[:6]:
            if a['type'] == 'error': st.error(f"**{a['time']}** | {a['msg']}")
            elif a['type'] == 'success': st.success(f"**{a['time']}** | {a['msg']}")
            else: st.info(f"**{a['time']}** | {a['msg']}")

# --- 6. MODULE: AI ANALYTICS ---
elif nav == "AI Analytics":
    st.title("📊 Safety Performance Analytics")
    
    # Impact Data
    data = pd.DataFrame({
        'Scenario': ['Manual Monitoring', 'Standard CCTV', 'SmartCrowd AI'],
        'Response Time (Min)': [18, 12, 2.8],
        'Accuracy (%)': [65, 82, 99]
    })
    
    c1, c2 = st.columns(2)
    with c1:
        fig1 = px.bar(data, x='Scenario', y='Response Time (Min)', color='Scenario', 
                     title="Reduction in Emergency Response Lag", template="plotly_dark")
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        fig2 = px.line(np.random.normal(0.5, 0.1, 100).cumsum(), 
                      title="AI Predictive Accuracy (Training Epochs)", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

# --- 7. MODULE: DEPLOYMENT ---
elif nav == "System Deployment":
    st.title("🚀 Implementation Roadmap")
    
    with st.expander("PHASE 1: Hardware Integration", expanded=True):
        st.write("- Edge-computing camera installation.")
        st.write("- Wi-Fi Mesh network for real-time triangulation.")
        st.progress(100)
        
    with st.expander("PHASE 2: Neural Network Training"):
        st.write("- Loading venue CAD models into the Digital Twin.")
        st.write("- Training surge-prediction algorithms.")
        st.progress(75)

    with st.expander("PHASE 3: Staff Ecosystem"):
        st.write("- Deployment of SmartCrowd mobile app for guards.")
        st.write("- Integration with Local Emergency Services (911/112).")
        st.progress(20)

    st.success("💡 System Scalability: Ready for venues up to 500k capacity.")