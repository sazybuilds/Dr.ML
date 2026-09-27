import streamlit as st
import requests
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

sys.path.append(str(PROJECT_ROOT))

from src.frontend.config.settings import Settings

settings = Settings()


API_URL = settings.api_url

st.set_page_config(
    page_title="Chronic Kidney Disease Prediction App",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Chronic Kidney Disease Prediction App")
st.write("Enter patient details and click **Predict**")

st.subheader("Patient Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age(Years)", 0, 120, 50)
    bp = st.number_input("Blood Pressure(mm/Hg)", 50, 200, 80)
    bgr = st.number_input("Blood Glucose Random(mgs/dl)", 20, 500, 120)
    bu = st.number_input("Blood Urea(mgs/dl)", 1, 400, 36)
    sc = st.number_input("Serum Creatinine(mgs/dl)", 0.0, 80.0, 1.2)
    sod = st.number_input("Sodium(mEq/L)", 100, 170, 135)
    pot = st.number_input("Potassium(mEq/L)", 2.0, 50.0, 4.5)
    hemo = st.number_input("Hemoglobin(gms)", 3.0, 20.0, 15.0)

with col2:
    pcv = st.number_input("Packed Cell Volume(%)", 9, 60, 44)
    wbcc = st.number_input("White Blood Cell Count(cells/cmm)", 2000, 30000, 8000)
    rbcc = st.number_input("Red Blood Cell Count(mill/cmm)", 2.0, 9.0, 5.0)
    sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025], index=3)
    al = st.selectbox("Albumin", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0], index=0)
    su = st.selectbox("Sugar", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0], index=0)
    rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"], format_func=lambda x: x.capitalize())
    pc = st.selectbox("Pus Cell", ["normal", "abnormal"], format_func=lambda x: x.capitalize())

with col3:
    pcc = st.selectbox("Pus Cell Clumps", ["notpresent", "present"], format_func=lambda x: "Present" if x == "present" else "Not Present")
    ba = st.selectbox("Bacteria", ["notpresent", "present"], format_func=lambda x: "Present" if x == "present" else "Not Present")
    htn = st.selectbox("Hypertension", ["no", "yes"], format_func=lambda x: "Yes" if x == "yes" else "No")
    dm = st.selectbox("Diabetes Mellitus", ["no", "yes"], format_func=lambda x: "Yes" if x == "yes" else "No")
    cad = st.selectbox("Coronary Artery Disease", ["no", "yes"], format_func=lambda x: "Yes" if x == "yes" else "No")
    appet = st.selectbox("Appetite", ["good", "poor"], format_func=lambda x: x.capitalize())
    pe = st.selectbox("Pedal Edema", ["no", "yes"], format_func=lambda x: "Yes" if x == "yes" else "No")
    ane = st.selectbox("Anemia", ["no", "yes"], format_func=lambda x: "Yes" if x == "yes" else "No")

if st.button("🔍 Predict", use_container_width=True):
    input_data = {
        "disease": "chronic_kidney_disease",
        "features": {
            "age": age,
            "bp": bp,
            "sg": sg,
            "al": al,
            "su": su,
            "rbc": rbc,
            "pc": pc,
            "pcc": pcc,
            "ba": ba,
            "bgr": bgr,
            "bu": bu,
            "sc": sc,
            "sod": sod,
            "pot": pot,
            "hemo": hemo,
            "pcv": pcv,
            "wbcc": wbcc,
            "rbcc": rbcc,
            "htn": htn,
            "dm": dm,
            "cad": cad,
            "appet": appet,
            "pe": pe,
            "ane": ane
        }
    }
    
    try:
        response = requests.post(API_URL, json=input_data, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Error connecting to the prediction service: {e}")
        st.caption(str(e))
        st.stop()
        
    result = response.json()
    prediction = result["prediction"]
    probability = result["probability"]
    
    st.divider()
    
    # 0 ---> Has Disease
    # 1 ----> Does not have disease
    disease_prob = 1 - probability
    
    st.metric(
        "Kidney Disease Probability",
        f"{disease_prob * 100:.2f}%"
    )
    
    if prediction == 0:
        st.error(f"⚠️ High Risk of Chronic Kidney Disease")
        st.warning("Please consult a healthcare professional for a detailed medical checkup.")
    else:
        st.success(f"✅ Low Risk of Chronic Kidney Disease")
        st.info("Keep maintaining a healthy lifestyle!")
            

