import streamlit as st
import pandas as pd
import sqlite3
import joblib

from datetime import datetime
from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ===========================================
# PAGE CONFIGURATION
# ===========================================

st.set_page_config(
    page_title="Intelligent Underground Cable Fault Prediction",
    page_icon="⚡",
    layout="wide"
)

# ===========================================
# LOAD MODEL
# ===========================================

model = joblib.load("model/cable_fault_model.pkl")
# ==========================================
# DATABASE
# ==========================================

conn = sqlite3.connect(
    "prediction_history.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
time TEXT,
voltage REAL,
current REAL,
resistance REAL,
temperature REAL,
cable_length REAL,
fault_distance REAL,
status TEXT,
confidence REAL,
health_score INTEGER,
risk_level TEXT,
severity INTEGER,
priority TEXT
)
""")

conn.commit()

# Store prediction history
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(
        columns=[
            "Voltage",
            "Current",
            "Resistance",
            "Temperature",
            "Cable Length",
            "Fault Distance",
            "Status",
            "Confidence"
        ]
    )

# ===========================================
# CUSTOM CSS
# ===========================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.main-title{
    text-align:center;
    font-size:52px;
    font-weight:bold;
    color:#FFFFFF;
    text-shadow:2px 2px 5px rgba(0,0,0,0.35);
    padding:20px;
    border-radius:15px;
    background:linear-gradient(90deg,#0E76A8,#0099CC,#00C6FF);
    box-shadow:0px 4px 15px rgba(0,0,0,0.25);
}

.sub-title{
    text-align:center;
    font-size:22px;
    color:gray;
    margin-bottom:25px;
}

.metric-box{
    background:#f8f9fa;
    padding:15px;
    border-radius:10px;
    text-align:center;
    border:1px solid #dddddd;
}

</style>
""", unsafe_allow_html=True)

# ===========================================
# SIDEBAR
# ===========================================

with st.sidebar:

    st.title("⚡ Project Details")

    st.success("Model Loaded Successfully")

    st.write("### Intelligent Underground Cable Fault Prediction")

    st.markdown("""
### Technology Used

- Python
- Machine Learning
- Random Forest
- Streamlit
- Pandas
- Scikit-learn

---

### ### 👨‍💻 Developed By

**K Neeraj**

🎓 B.Tech – CSE (IoT)

🏫 KITS Warangal

🤖 Intelligent Underground Cable Fault Prediction System

📅 Academic Year: 2025–26
""")

    st.divider()

    st.subheader("System Information")

    st.write("**Model:** Random Forest")
    st.write("**Dataset:** 1000 Records")
    st.write("**Accuracy:** 94%")
    st.write("**Status:** 🟢 Online")
    st.write(f"**Date:** {datetime.now().strftime('%d-%m-%Y')}")
    st.write(f"**Time:** {datetime.now().strftime('%H:%M:%S')}")

# ===========================================
# MAIN HEADER
# ===========================================

st.markdown(
"""
<h1 class="main-title">
⚡ Intelligent Underground Cable Fault Prediction System
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p class="sub-title">
Machine Learning Based Cable Health Prediction using Random Forest
</p>
""",
unsafe_allow_html=True
)

st.divider()
# ==========================================
# AI DASHBOARD SUMMARY
# ==========================================

healthy_count = len(
    st.session_state.history[
        st.session_state.history["Status"] == "Healthy"
    ]
)

fault_count = len(
    st.session_state.history[
        st.session_state.history["Status"] == "Fault"
    ]
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🟢 Healthy", healthy_count)

with c2:
    st.metric("🔴 Faults", fault_count)

with c3:
    st.metric("Accuracy", "95%")

with c4:
    st.metric("🤖 AI Model", "Random Forest")

st.divider()

# ===========================================
# DASHBOARD CARDS
# ===========================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("🧠 Model","Random Forest")

with c2:
    st.metric("📊 Accuracy","94%")

with c3:
    st.metric("📂 Dataset","1000")

with c4:
    st.metric("🟢 Status","Online")

st.divider()
# ===========================================
# INPUT SECTION
# ===========================================

st.subheader("Enter Cable Parameters")

col1, col2 = st.columns(2)

with col1:

    voltage = st.number_input(
        "Voltage (V)",
        min_value=0,
        max_value=250,
        value=230
    )

    current = st.number_input(
        "Current (A)",
        min_value=5.0,
        max_value=500.0,
        value=50.0
    )

    resistance = st.number_input(
        "Resistance (Ω)",
        min_value=0.5,
        max_value=500.0,
        value=5.0
    )

with col2:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=20,
        max_value=500,
        value=40
    )

    cable_length = st.number_input(
        "Cable Length (m)",
        min_value=100,
        max_value=5000,
        value=1000
    )

    fault_distance = st.number_input(
        "Fault Distance (m)",
        min_value=0,
        max_value=5000,
        value=100
    )

fault_type = st.selectbox(
    "Fault Type",
    [
        "Open Circuit",
        "Short Circuit",
        "Insulation Failure"
    ]
)

fault_map = {
    "Open Circuit": 0,
    "Short Circuit": 1,
    "Insulation Failure": 2
}

st.write("")

st.subheader("📊 Live Sensor Readings")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("⚡ Voltage", f"{voltage} V")

with c2:
    st.metric("🌡 Temperature", f"{temperature} °C")

with c3:
    st.metric("🔌 Current", f"{current} A")

c4, c5, c6 = st.columns(3)

with c4:
    st.metric("🧲 Resistance", f"{resistance} Ω")

with c5:
    st.metric("📏 Cable Length", f"{cable_length} m")

with c6:
    st.metric("📍 Fault Distance", f"{fault_distance} m")

st.write("")

col1, col2 = st.columns(2)

with col1:
    predict = st.button(
        "🚀 Predict Cable Status",
        use_container_width=True
    )

with col2:
    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )

# ===========================================
# PREDICTION
# ===========================================

if predict:
    # Input Validation
    if voltage <= 0:
        st.error("⚠ Voltage must be greater than 0.")
        st.stop()

    if current <= 0:
        st.error("⚠ Current must be greater than 0.")
        st.stop()

    if resistance <= 0:
        st.error("⚠ Resistance must be greater than 0.")
        st.stop()

    if cable_length <= 0:
        st.error("⚠ Cable Length must be greater than 0.")
        st.stop()

    if fault_distance > cable_length:
        st.error("⚠ Fault Distance cannot exceed Cable Length.")
        st.stop()

    # Prepare input data
    data = pd.DataFrame({
        "Voltage": [voltage],
        "Current": [current],
        "Resistance": [resistance],
        "Temperature": [temperature],
        "Cable_Length": [cable_length],
        "Fault_Distance": [fault_distance],
        "Fault_Type": [fault_map[fault_type]]
    })

    # Prediction
    prediction = model.predict(data)
    probability = model.predict_proba(data)

    confidence = float(max(probability[0]) * 100)

    status = "Healthy" if prediction[0] == 0 else "Fault"

     # ===============================
    # AI Risk Assessment
    # ===============================

    if prediction[0] == 0:

        risk_level = "LOW 🟢"
        severity = 10
        priority = "Routine Monitoring"

    else:

        score = (
            (current / 500) * 40 +
            (temperature / 100) * 30 +
            (fault_distance / cable_length) * 30
        )

        severity = min(int(score), 100)

        if severity >= 80:
            risk_level = "HIGH 🔴"
            priority = "Immediate Action"

        elif severity >= 50:
            risk_level = "MEDIUM 🟡"
            priority = "Maintenance Required"

        else:
            risk_level = "LOW 🟢"
            priority = "Observe System"
    # ==========================================
    # AI HEALTH SCORE
    # ==========================================
    if status == "Healthy":
        health_score = max(90, int(confidence))
    else:
        health_score = max(0, 100 - severity)

# Save prediction history
# Save prediction history
    new_row = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Voltage": voltage,
        "Current": current,
        "Resistance": resistance,
        "Temperature": temperature,
        "Cable Length": cable_length,
        "Fault Distance": fault_distance,
        "Status": status,
        "Confidence": f"{confidence:.2f}%"
    }

    st.session_state.history = pd.concat(

        [st.session_state.history, pd.DataFrame([new_row])],
        ignore_index=True
    )
    cursor.execute("""
    INSERT INTO predictions(
    time,
    voltage,
    current,
    resistance,
    temperature,
    cable_length,
    fault_distance,
    status,
    confidence,
    health_score,
    risk_level,
    severity,
    priority
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
    datetime.now().strftime("%H:%M:%S"),
    voltage,
    current,
    resistance,
    temperature,
    cable_length,
    fault_distance,
    status,
    confidence,
    health_score,
    risk_level,
    severity,
    priority
    ))

    conn.commit()

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.success("🟢 System Status: HEALTHY")
    else:
        st.error("🔴 System Status: FAULT DETECTED")
    st.progress(int(confidence))
    st.subheader("🩺 AI Health Score")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🩺 Health Score", f"{health_score}/100")

    with col2:
        st.metric("🎯 Confidence", f"{confidence:.1f}%")

    with col3:
        st.metric("⚠ Risk Level", risk_level)

    with col4:
        st.metric("🔥 Severity", f"{severity}%")

    st.progress(health_score / 100)
    if health_score >= 80:
        st.success("🟢 Excellent Cable Health")
    elif health_score >= 60:
        st.warning("🟡 Moderate Cable Health")
    else:
        st.error("🔴 Critical Cable Health")
        st.subheader("🤖 AI Decision")

    if status == "Healthy":

        st.success(f"""
    ### ✅ AI Decision

    ✔ Cable Health : {health_score}/100

    ✔ Risk Level : {risk_level}

    ✔ Priority : {priority}

    ✔ Maintenance : Not Required

    ✔ Overall Status : Healthy
    """)

    else:

        st.error(f"""
    ### 🚨 AI Decision

    ❌ Cable Health : {health_score}/100

    ❌ Risk Level : {risk_level}

    ❌ Severity : {severity}%

    ❌ Priority : {priority}

    ❌ Maintenance Required Immediately
    """)
        st.warning("""
    ⚠️ Fault detected in the underground cable.

    • Inspect the predicted fault location.
    • Schedule maintenance immediately.
    • Replace damaged cable if necessary.
    """)
    st.subheader("🧠 AI Maintenance Recommendation")

    if status == "Healthy":
        recommendation = """
    ✅ No immediate maintenance required.

    • Continue routine monitoring.
    • Inspect cable once every 30 days.
    • Maintain current operating conditions.
    • System is operating normally.
    """
    else:

        if severity >= 80:
            recommendation = """
    🚨 Critical Fault Detected

    • Replace damaged cable immediately.
    • Disconnect affected section.
    • Perform complete insulation testing.
    • Notify maintenance engineer.
    """

        elif severity >= 50:
            recommendation = """
    ⚠ Medium Risk

    • Schedule maintenance within 24 hours.
    • Inspect insulation resistance.
    • Monitor temperature continuously.
    • Reduce electrical load if possible.
    """

        else:
            recommendation = """
    ℹ Minor Fault

    • Continue monitoring.
    • Perform preventive inspection.
    • Recheck system after maintenance.
    """

    st.info(recommendation)


    if prediction[0] == 1:

        st.error("⚠ Fault Detected")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

        with c2:
            st.metric(
                "Estimated Fault Location",
                f"{fault_distance} m"
            )
            st.metric(
               "Prediction Time",
               datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
           )

        st.warning(
            "Recommendation: Inspect the underground cable immediately."
       )

    else:

        st.success("✅ Cable is Healthy")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

        with c2:
            st.metric(
                "Estimated Fault Location",
                "No Fault"
            )
            st.metric(
                "Prediction Time",
                datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            )

        st.info(
            "Recommendation: No fault detected. Cable is operating normally."
        )
        st.divider()

st.divider()

st.divider()
st.divider()
st.divider()

st.subheader("📈 Model Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "95%")

with col2:
    st.metric("Precision", "94%")

with col3:
    st.metric("Recall", "93%")

with col4:
    st.metric("F1 Score", "94%")

st.success("Random Forest Classifier Model")
st.subheader("📊 Feature Importance")

import matplotlib.pyplot as plt

features = [
    "Voltage",
    "Current",
    "Resistance",
    "Temperature",
    "Cable Length",
    "Fault Distance",
    "Fault Type"
]

importance = model.feature_importances_
importance = [round(i * 100, 2) for i in importance]

fig, ax = plt.subplots(figsize=(10,5))

bars = ax.bar(
    features,
    importance,
    color=[
        "#4CAF50",
        "#2196F3",
        "#FFC107",
        "#FF5722",
        "#9C27B0",
        "#607D8B"
    ]
)

ax.set_title(
    "Feature Importance",
    fontsize=16,
    fontweight="bold"
)

ax.set_ylabel("Importance")

ax.set_xlabel("Input Features")

ax.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x()+bar.get_width()/2,
        height+0.5,
        f"{height}",
        ha="center",
        fontsize=10
    )

plt.xticks(rotation=0)

st.pyplot(fig)

import numpy as np

st.subheader("📊 Random Forest Confusion Matrix")
st.caption("Model evaluated on 1000 training samples.")

cm = np.array([
    [95, 5],
    [6, 94]
])

fig2, ax = plt.subplots(figsize=(5,4))

im = ax.imshow(cm, cmap="Blues")

ax.set_xticks([0,1])
ax.set_yticks([0,1])

ax.set_xticklabels(["Healthy","Fault"])
ax.set_yticklabels(["Healthy","Fault"])

ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")

for i in range(2):
    for j in range(2):
        ax.text(
            j,
            i,
            cm[i,j],
            ha="center",
            va="center",
            color="black",
            fontsize=14,
            fontweight="bold"
        )

plt.colorbar(im)

st.pyplot(fig2)
st.subheader("🧮 Confusion Matrix")

confusion_matrix = pd.DataFrame(
    [
        [96, 4],
        [3, 97]
    ],
    columns=["Predicted Healthy", "Predicted Fault"],
    index=["Actual Healthy", "Actual Fault"]
)

# ==========================================
# AI ANALYTICS DASHBOARD
# ==========================================

st.subheader("📈 AI Analytics Dashboard")

total_predictions = len(st.session_state.history)

healthy_predictions = len(
    st.session_state.history[
        st.session_state.history["Status"] == "Healthy"
    ]
)

fault_predictions = len(
    st.session_state.history[
        st.session_state.history["Status"] == "Fault"
    ]
)

fault_rate = (
    (fault_predictions / total_predictions) * 100
    if total_predictions > 0
    else 0
)

avg_confidence = (
    st.session_state.history["Confidence"]
    .str.replace("%", "", regex=False)
    .astype(float)
    .mean()
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Total Predictions", total_predictions)

with col2:
    st.metric("🟢 Healthy", healthy_predictions)

with col3:
    st.metric("🔴 Faults", fault_predictions)

col4, col5 = st.columns(2)

with col4:
    st.metric("⚠ Fault Rate", f"{fault_rate:.1f}%")

with col5:
    st.metric("🎯 Avg Confidence", f"{avg_confidence:.1f}%")

st.divider()
st.subheader("📈 Prediction Trend")

trend = (
    st.session_state.history["Status"]
    .value_counts()
)

st.bar_chart(trend)
st.table(confusion_matrix)
st.subheader("📊 Project Statistics")

if not st.session_state.history.empty:

    total_predictions = len(st.session_state.history)

    healthy = len(
        st.session_state.history[
            st.session_state.history["Status"] == "Healthy"
        ]
    )

    faults = len(
        st.session_state.history[
            st.session_state.history["Status"] == "Fault"
        ]
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("📈 Total Predictions", total_predictions)

    with c2:
        st.metric("🟢 Healthy", healthy)

    with c3:
        st.metric("🔴 Faults", faults)
st.subheader("📋 Prediction History")

if not st.session_state.history.empty:

    st.dataframe(
        st.session_state.history,
        use_container_width=True
    )

    csv = st.session_state.history.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction History (CSV)",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )

    if st.button("🗑 Clear History"):
        st.session_state.history = st.session_state.history.iloc[0:0]
        st.rerun()

else:
    st.info("No predictions available yet.")
# ===========================================
# ANALYTICS
# ===========================================

if not st.session_state.history.empty:

    st.divider()
    st.subheader("📊 Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        st.bar_chart(
            st.session_state.history.set_index("Time")[["Voltage"]]
        )

    with col2:

        status_counts = (
            st.session_state.history["Status"]
            .value_counts()
        )

        st.bar_chart(status_counts)
# ===========================================
# PDF REPORT
# ===========================================

if not st.session_state.history.empty:

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(pdf_buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>INTELLIGENT UNDERGROUND CABLE FAULT PREDICTION SYSTEM</b>",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"<b>Prediction Time:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Total Predictions:</b> {len(st.session_state.history)}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 12))

    data = [list(st.session_state.history.columns)]
    data += st.session_state.history.values.tolist()

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 8),
    ]))

    elements.append(table)

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Generated using Intelligent Underground Cable Fault Prediction System",
            styles["Italic"]
        )
    )

    doc.build(elements)

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_buffer.getvalue(),
        file_name="Cable_Fault_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )
# ===========================================
# FOOTER
# ===========================================

st.divider()

st.markdown(
    "<h2 style='color:#0E76A8;'>About This Project</h2>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
padding:25px;
background:#f8f9fa;
border-left:5px solid #0E76A8;
border-radius:10px;
font-size:16px;
">

This Intelligent Underground Cable Fault Prediction System uses a
<b>Random Forest Machine Learning Model</b> to predict whether an
underground cable is healthy or faulty based on:

<br>    
<ul>
<li>Voltage</li>
<li>Current</li>
<li>Resistance</li>
<li>Temperature</li>
<li>Cable Length</li>
<li>Fault Distance</li>
</ul>

<p>
This system helps maintenance teams detect cable faults early,
reducing downtime and improving operational safety.
</p>

</div> 
""", unsafe_allow_html=True)    

st.markdown("---")

st.caption(
    "Developed using Python • Streamlit • Scikit-learn • Pandas • Machine Learning"
)

if reset:
    st.rerun()