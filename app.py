import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/cable_fault_model.pkl")

st.title("Intelligent Underground Cable Fault Prediction System")

voltage = st.number_input("Voltage", 210, 250, 230)
current = st.number_input("Current", 5.0, 100.0, 50.0)
resistance = st.number_input("Resistance", 0.5, 20.0, 5.0)
temperature = st.number_input("Temperature", 20, 90, 40)
cable_length = st.number_input("Cable Length", 100, 5000, 1000)
fault_distance = st.number_input("Fault Distance", 0, 5000, 100)

fault_type = st.selectbox(
    "Fault Type",
    ["Open Circuit", "Short Circuit", "Insulation Failure"]
)

fault_map = {
    "Open Circuit": 0,
    "Short Circuit": 1,
    "Insulation Failure": 2
}

if st.button("Predict"):

    data = pd.DataFrame({
        "Voltage":[voltage],
        "Current":[current],
        "Resistance":[resistance],
        "Temperature":[temperature],
        "Cable_Length":[cable_length],
        "Fault_Distance":[fault_distance],
        "Fault_Type":[fault_map[fault_type]]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠ Fault Detected")
    else:
        st.success("✅ Cable is Healthy")