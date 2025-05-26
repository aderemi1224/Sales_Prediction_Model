
import streamlit as st
import pandas as pd
import joblib

# Load models
rf_model = joblib.load("random_forest_model.pkl")
lin_model = joblib.load("linear_model.pkl")

st.title("Sales Prediction App")

model_option = st.selectbox("Choose a Model", ["Random Forest", "Linear Regression"])

# Replace these with your actual features
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

input_data = pd.DataFrame({
    "Feature1": [feature1],
    "Feature2": [feature2],
    "Feature3": [feature3]
})

if st.button("Predict Sales Amount"):
    model = rf_model if model_option == "Random Forest" else lin_model
    prediction = model.predict(input_data)
    st.success(f"Predicted Sales Amount: {prediction[0]:,.2f}")
