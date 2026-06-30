import streamlit as st
import pandas as pd
import joblib

# ============================
# Prediction History
# ============================

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
    font-size:48px;
    color:#0E76A8;
    font-weight:bold;
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

### Developed By

Neeraj

AI Internship Project
""")

    st.divider()

    st.subheader("System Information")

    st.write("**Model:** Random Forest")
    st.write("**Dataset:** 1000 Records")
    st.write("**Accuracy:** 94%")
    st.write("**Status:** 🟢 Online")

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
        min_value=210,
        max_value=250,
        value=230
    )

    current = st.number_input(
        "Current (A)",
        min_value=5.0,
        max_value=100.0,
        value=50.0
    )

    resistance = st.number_input(
        "Resistance (Ω)",
        min_value=0.5,
        max_value=20.0,
        value=5.0
    )

with col2:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=20,
        max_value=90,
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

# ===========================================
# PREDICTION
# ===========================================

if predict:

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

    # Save prediction history
    new_row = {
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

    st.divider()

    st.subheader("Prediction Result")

    st.progress(int(confidence))

    st.markdown(
        f"### Overall Prediction Confidence: **{confidence:.2f}%**"
    )

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

        st.info(
            "Recommendation: No fault detected. Cable is operating normally."
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

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Developer**")
        st.success("Neeraj")

    with col2:
        st.write("**Project**")
        st.success("AI Internship Project")

    st.caption(
        "Developed using Python • Streamlit • Scikit-learn • Pandas • Machine Learning"
    )
    if reset:
    st.rerun()