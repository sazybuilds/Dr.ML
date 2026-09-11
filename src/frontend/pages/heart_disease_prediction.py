# pyrefly: ignore [missing-import]
import streamlit as st
import os
import requests

from src.frontend.config.settings import Settings

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[3]

sys.path.append(str(PROJECT_ROOT))


settings = Settings()

API_URL = settings.api_url


st.set_page_config(
    page_title="HeartDiseaseAssistant",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Heart Disease predictor")

st.subheader("Enter patient details and click **Predict**")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120, 52)
    sex = st.selectbox("Sex(1=Male, 0=Female)", [0, 1])
    cp = st.number_input("Chest Pain Type (cp)", 0, 3, 0)
    trestbps = st.number_input("Resting Blood Pressure", 0, 250, 125)
    chol = st.number_input("Cholesterol", 0, 600, 212)


with col2:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.number_input("Resting ECG (restecg)", 0, 2, 1)
    thalach = st.number_input("Max Heart Rate (thalach)", 0, 250, 168)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])



with col3:
    oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 10.0, 1.0)
    slope = st.number_input("Slope", 0, 2, 2)
    ca = st.number_input("Number of Major Vessels (ca)", 0, 4, 0)
    thal = st.number_input("Thal", 0, 3, 2)



if st.button("🔍Predict"):
    input_data = {
            "disease": "heart_disease",
            "features": {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }
    }
    try:
        response = requests.post(API_URL, json=input_data, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error("Unable to reach prediction service.")
        st.caption(str(e))
        st.stop()

    result = response.json()
    prediction = int(result["prediction"])
    probability = float(result["probability"])

    st.divider()

    st.metric(
        label="Heart Disease Probability",
        value=f"{(probability)*100:.3f}%"
    )
    if prediction == 1:
        st.error(f"⚠️Model Prediction: {prediction}")
    else:
        st.success(f"✅Model Prediction: {prediction}")

    #TODO: Create production UI using HTML, CSS and JavaScript









