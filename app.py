import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="GenAI SOC Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🛡️ GenAI-Powered SOC Analyst Assistant")
st.caption("Healthcare Cybersecurity Monitoring Dashboard")

st.divider()

# -----------------------------
# Pipeline Selection
# -----------------------------
pipeline = st.radio(
    "Select Processing Pipeline",
    ["With SIEM", "Without SIEM"],
    horizontal=True
)

# -----------------------------
# Total Alerts
# -----------------------------
col1, col2 = st.columns([1,3])

with col1:
    st.metric(
        label="🚨 Total Alerts",
        value="128"
    )

# -----------------------------
# Sample Alert Graph
# -----------------------------
with col2:

    df = pd.DataFrame({
        "Time":[
            "09:00","09:30","10:00","10:30",
            "11:00","11:30","12:00","12:30"
        ],
        "Alerts":[12,20,18,35,24,30,28,40]
    })

    fig = px.line(
        df,
        x="Time",
        y="Alerts",
        markers=True,
        title="Alert Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.success(f"Current Pipeline : {pipeline}")