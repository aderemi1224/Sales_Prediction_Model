import streamlit as st
import pandas as pd
import joblib

# Load models
rf_model = joblib.load("Sales_Prediction_Model/random_forest_model.pkl")
lin_model = joblib.load("Sales_Prediction_Model/linear_model.pkl")

st.title("Sales Prediction App")

model_option = st.selectbox("Choose a Model", ["Random Forest", "Linear Regression"])

# Numerical feature inputs
cost_price = st.number_input("Cost Price")
unit_price = st.number_input("Unit Price")
quantity = st.number_input("Quantity")
profit = st.number_input("Profit")
age = st.number_input("Customer Age")

# Categorical feature inputs
region = st.selectbox("Region", ["East", "South", "West"])  # adjust if you have more/less
marital_status = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])
product_category = st.selectbox("Product Category", ["Furniture", "Toys", "Office Supplies"])  # adjust to your dataset
gender = st.selectbox("Gender", ["Male", "Female"])

# Combine inputs into a DataFrame
input_data = pd.DataFrame({
    "Cost Price": [cost_price],
    "Unit Price": [unit_price],
    "Quantity": [quantity],
    "Profit": [profit],
    "Age": [age],
    "Region": [region],
    "Marital Status": [marital_status],
    "Product Category": [product_category],
    "Gender": [gender]
})

# Prediction logic
if st.button("Predict Sales Amount"):
    model = rf_model if model_option == "Random Forest" else lin_model
    prediction = model.predict(input_data)
    st.success(f"Predicted Sales Amount: {prediction[0]:,.2f}")
