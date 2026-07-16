import streamlit as st
from predict import predict_heart_risk

st.set_page_config(
    page_title="AI Health Risk Predictor",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ AI Health Risk Predictor")
st.write("Predict the risk of Heart Disease using Machine Learning")

st.sidebar.header("Enter Patient Details")

age = st.sidebar.number_input("Age", 20, 100, 50)
sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.sidebar.slider("Chest Pain Type", 0, 3, 1)
trestbps = st.sidebar.number_input("Resting Blood Pressure", 80, 250, 120)
chol = st.sidebar.number_input("Cholesterol", 100, 600, 200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.sidebar.slider("Resting ECG", 0, 2, 1)
thalach = st.sidebar.number_input("Max Heart Rate", 60, 220, 150)
exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.sidebar.slider("Old Peak", 0.0, 6.0, 1.0)
slope = st.sidebar.slider("Slope", 0, 2, 1)
ca = st.sidebar.slider("Major Vessels", 0, 4, 0)
thal = st.sidebar.slider("Thal", 0, 3, 2)

if st.button("🔍 Predict Risk"):

    features = [
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        ca, thal
    ]

    prediction, probability = predict_heart_risk(features)

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.metric(
        "Risk Probability",
        f"{probability * 100:.2f}%"
    )