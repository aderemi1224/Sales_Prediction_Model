#  **Sales Prediction App** built using trained models and deployed with streamlit:

---


### 🛍️ Sales Prediction App

This is a simple web application built using [Streamlit](https://streamlit.io/) that allows users to predict **sales amounts** based on key product, demographic, and pricing features. It supports two types of machine learning models: **Random Forest** and **Linear Regression**.

---

### 🚀 Features

- Interactive form to input sales-related features:
  - Numerical: `Cost Price`, `Unit Price`, `Quantity`, `Profit`, `Age`
  - Categorical: `Region`, `Marital Status`, `Product Category`, `Gender`
- Toggle between Random Forest and Linear Regression models
- Get instant sales predictions

---

## 📦 Requirements

- Python 3.7+
- Installed Python packages:
  ```bash
  pip install streamlit pandas joblib scikit-learn
````

## 🧠 Models Used

* **Random Forest Regressor**
* **Linear Regression**

Both models were trained using the same feature set and a shared preprocessing pipeline (e.g., one-hot encoding for categorical variables).

Models should be saved in the directory `Sales_Prediction_Model/` as:

* `random_forest_model.pkl`
* `linear_model.pkl`

Each `.pkl` file should include the full pipeline (preprocessing + model).

---

## 🛠 How to Run the App

```bash
streamlit run app.py
```

Make sure `app.py` and your `Sales_Prediction_Model` folder (with the `.pkl` files) are in the same directory.

---

## 📋 Inputs Required

### 🔢 Numerical Features

* **Cost Price**
* **Unit Price**
* **Quantity**
* **Profit**
* **Age**

### 🧑‍🤝‍🧑 Categorical Features

* **Region** (e.g., North, South, East, West)
* **Marital Status** (e.g., Single, Married)
* **Product Category** (e.g., Food, Beverage, Household)
* **Gender** (e.g., Male, Female)

---

## 🧪 Output

* The predicted **Sales Amount** based on the selected model and user input.

---

## 📁 Project Structure

```
Sales_Prediction_App/
│
├── app.py
├── Sales_Prediction_Model/
│   ├── random_forest_model.pkl
│   └── linear_model.pkl
└── README.md
```

