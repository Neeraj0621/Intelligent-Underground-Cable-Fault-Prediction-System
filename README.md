![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random_Forest-orange?logo=scikitlearn)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-Educational-green)
# Intelligent Underground Cable Fault Prediction System

## 📌 Project Overview

The **Intelligent Underground Cable Fault Prediction System** is an AI-powered web application developed using **Python, Streamlit, Scikit-learn, and SQLite**. The system uses a **Random Forest Classifier** to analyze electrical and environmental parameters and predict whether an underground cable is **Healthy** or **Faulty**.

The application provides real-time fault prediction, AI-based health scoring, risk level analysis, maintenance recommendations, analytics dashboards, feature importance visualization, PDF report generation, CSV export, and persistent prediction history using SQLite. It is designed to demonstrate how Artificial Intelligence can support predictive maintenance in power distribution systems.

---

## 🚀 Key Highlights

- AI-based Underground Cable Fault Prediction
- Random Forest Machine Learning Model
- AI Health Score & Risk Assessment
- Interactive Analytics Dashboard
- SQLite Database for Prediction History
- PDF & CSV Report Generation
- Feature Importance Visualization
- Confusion Matrix for Model Evaluation
- Responsive Streamlit Web Application

## ✨ Features

- 🤖 AI-powered Underground Cable Fault Prediction
- 🌲 Random Forest Machine Learning Model
- 🩺 AI Health Score Analysis
- ⚠️ Risk Level & Severity Assessment
- 💡 Intelligent Maintenance Recommendations
- 📊 Interactive Analytics Dashboard
- 📈 Feature Importance Visualization
- 📉 Confusion Matrix
- 📝 Prediction History
- 🗄️ SQLite Database Integration
- 📄 PDF Report Generation
- 📥 CSV Export
- 📱 Responsive Streamlit Interface

---
## Application Screenshots

### Home Page

![Home](screenshots/home.png)

### Prediction Result

![Prediction](screenshots/prediction.png)

### Analytics Dashboard

![Dashboard](screenshots/dashboard.png)
## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- ReportLab

---

## 🤖 Machine Learning Model

| Parameter | Value |
|-----------|-------|
| Algorithm | Random Forest Classifier |
| Dataset Size | 1000 Records |
| Input Features | 7 |
| Target Variable | Cable Fault (Healthy/Fault) |
| Model Accuracy | 95% |
| Feature Importance | Temperature, Resistance, Current, Voltage, Fault Distance, Cable Length, Fault Type |

---

## Input Parameters

- Voltage
- Current
- Resistance
- Temperature
- Cable Length
- Fault Distance
- Fault Type

---

## Output

- Healthy / Fault Prediction
- Prediction Confidence
- Estimated Fault Location
- Recommendation

---

## 📂 Project Structure

```text
Intelligent-Underground-Cable-Fault-Prediction-System
│
├── app.py                        # Streamlit Application
├── train_model.py                # Model Training Script
├── requirements.txt              # Python Dependencies
├── README.md                     # Project Documentation
├── dataset/
│   └── cable_fault_dataset.csv
├── model/
│   └── cable_fault_model.pkl
├── screenshots/
│   ├── home.png
│   ├── prediction.png
│   └── dashboard.png
├── documents/
└── prediction_history.db
```
---

## 👨‍💻 Developer

**K. Neeraj**

**B.Tech – Computer Science and Engineering (Internet of Things)**

Kakatiya Institute of Technology and Science (KITS), Warangal

**Project Type:** AI & Machine Learning Internship Project

**Technologies:** Python, Streamlit, Scikit-learn, SQLite, Pandas, NumPy, Matplotlib, ReportLab

---

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---
## 🔮 Future Scope

- Integration with IoT sensors for real-time monitoring
- Cloud database support for centralized data storage
- Mobile application for remote monitoring
- Email and SMS alerts for critical cable faults
- Deep Learning models for enhanced prediction accuracy
- GIS-based cable fault location visualization
- Real-time dashboard with live sensor streaming

## License

This project was developed for academic and educational purposes.