import streamlit as st
import pandas as pd
import joblib

# Load the model and feature names
model = joblib.load("random_forest_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("🚨 Human Trafficking Risk Prediction")
st.write("Provide the details below to predict the risk level for trafficking cases.")

# Predefined options based on your training data
regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']  # From dataset
subregions = [
    'Central Asia', 'Eastern Africa', 'Western Africa', 'Southern Asia',
    'Northern Europe', 'South America', 'Caribbean', 'Eastern Europe'
]
forms_of_trafficking = [
    'Sexual Exploitation',
    'Forced Labour',
    'Other Perpetrator known to the victim',
    'Perpetrator unknown to the victim',
    'Sexual violence',
    'Sexual violence: Other acts of sexual violence',
    'Sexual violence: Rape',
    'Sexual violence: Sexual assault'
]

# User inputs
region = st.selectbox("🌍 Region", regions)
subregion = st.selectbox("📍 Subregion", subregions)
form = st.selectbox("📌 Form of Trafficking Reported", forms_of_trafficking)
value = st.number_input("📊 Value", min_value=0.0, max_value=1.0, step=0.01)

# Build input dataframe
input_data = pd.DataFrame(columns=feature_names)
input_data.loc[0] = 0  # Default all to zero

# One-hot encode user inputs based on training feature names
if f"Region_{region}" in input_data.columns:
    input_data[f"Region_{region}"] = 1
if f"Subregion_{subregion}" in input_data.columns:
    input_data[f"Subregion_{subregion}"] = 1
if f"Category_{form}" in input_data.columns:
    input_data[f"Category_{form}"] = 1

if "Value" in input_data.columns:
    input_data["Value"] = value

# Predict
if st.button("Predict Risk Level"):
    proba_high_risk = model.predict_proba(input_data)[0][1] * 100  # Probability of class 1 (high risk)

    if proba_high_risk >= 50:
        st.error(f"High Risk ⚠️\nRisk Probability: {proba_high_risk:.2f}%")
    else:
        st.success(f"Low Risk ✅\nRisk Probability: {proba_high_risk:.2f}%")
