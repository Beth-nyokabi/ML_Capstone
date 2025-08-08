import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model and features
model = joblib.load("random_forest_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.set_page_config(page_title="Trafficking Risk Predictor", layout="centered")

st.title("🚨 Human Trafficking Risk Prediction App")
st.write("Enter country-level data to predict if it's at high risk for sexual exploitation-related trafficking.")

# --- User Inputs ---
age_0_14 = st.slider("Population aged 0-14 (%)", 0.0, 50.0, 20.0)
age_15_64 = st.slider("Population aged 15-64 (%)", 0.0, 80.0, 60.0)
female_employment = st.slider("Female employment rate (%)", 0.0, 100.0, 50.0)
internet_users = st.slider("Internet users (%)", 0.0, 100.0, 40.0)
gender_inequality = st.slider("Gender Inequality Index", 0.0, 1.0, 0.4)

category = st.selectbox("Category of Violence", [
    "Other Perpetrator known to the victim",
    "Perpetrator unknown to the victim",
    "Relationship to perpetrator is not known",
    "Sexual Exploitation",
    "Sexual violence: Other acts of sexual violence",
    "Sexual violence: Rape or attempted rape",
    "Trafficking"
])

# --- Prepare Input ---
input_dict = {
    'Age_0_14': age_0_14,
    'Age_15_64': age_15_64,
    'Female_employment_rate': female_employment,
    'Internet_users': internet_users,
    'Gender_Inequality_Index': gender_inequality,
    'Category': category
}

input_df = pd.DataFrame([input_dict])

# --- One-Hot Encode like training ---
input_df = pd.get_dummies(input_df)

# Add missing columns with 0, reindex to match training features
input_df = input_df.reindex(columns=feature_names, fill_value=0)

# --- Make Prediction ---
if st.button("🔍 Predict Risk"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][int(prediction)]

    if prediction == 1:
        st.error(f"🔴 High Risk of Sexual Exploitation (Confidence: {proba:.2%})")
    else:
        st.success(f"🟢 Low Risk (Confidence: {proba:.2%})")

# --- Optional: Feature Importances ---
if st.checkbox("📊 Show Feature Importance"):
    importances = model.named_steps['rf'].feature_importances_
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    st.subheader("Top 15 Important Features")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x="Importance", y="Feature", data=importance_df.head(15), ax=ax)
    st.pyplot(fig)
