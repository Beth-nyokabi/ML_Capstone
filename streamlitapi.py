import streamlit as st
import pandas as pd
import joblib

# === Load the model and feature names ===
model = joblib.load("final_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# === Page Configuration ===
st.set_page_config(page_title="Trafficking Risk Classifier", layout="centered")

st.title("🚨 Human Trafficking Risk Classifier")
st.markdown("Enter country-specific indicators to predict whether a country is **High Risk (1)** or **Low Risk (0)** for human trafficking.")

# === User Input Section ===

st.subheader("📥 Input Country Indicators")

year = st.slider("Year", min_value=1990, max_value=2025, value=2020)

victim_female = st.selectbox("Victim Female Proportion High?", ["Yes", "No"])
violence_reported = st.selectbox("Sexual Violence Reported?", ["Yes", "No"])

# These categories should match those in your dataset — adjust them as needed
region = st.selectbox("Region", ["Africa", "Americas", "Asia", "Europe", "Oceania"])
subregion = st.selectbox("Subregion", [
    "Eastern Africa", "Middle Africa", "Northern Africa", "Southern Africa", "Western Africa",
    "Caribbean", "Central America", "South America", "Northern America",
    "Central Asia", "Eastern Asia", "South-Eastern Asia", "Southern Asia", "Western Asia",
    "Eastern Europe", "Northern Europe", "Southern Europe", "Western Europe",
    "Australia and New Zealand", "Melanesia", "Micronesia", "Polynesia"
])
category = st.selectbox("Form of Trafficking Reported", [
    "Forced Labour", "Forced Marriage", "Organ Removal", "Other", "Perpetrator known to the victim",
    "Perpetrator unknown to the victim", "Relationship to perpetrator is not known", 
    "Sexual Exploitation", "Sexual violence: Other acts of sexual violence"
])

# === Build input row as dictionary ===
input_data = {
    "Year": year,
    "Victim Female Proportion High": 1 if victim_female == "Yes" else 0,
    "Sexual violence reported": 1 if violence_reported == "Yes" else 0,
    f"Region_{region}": 1,
    f"Subregion_{subregion}": 1,
    f"Category_{category}": 1
}

# === Initialize all other features with 0 ===
input_df = pd.DataFrame(columns=feature_names)
input_df.loc[0] = 0  # Fill all with 0

# === Update input_df with actual user values ===
for feature, value in input_data.items():
    if feature in input_df.columns:
        input_df.at[0, feature] = value

# === Prediction ===
if st.button("🚀 Predict Trafficking Risk"):
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0][prediction]

    st.markdown("### 🧠 Prediction Result")
    if prediction == 1:
        st.error(f"🔴 High Risk of Human Trafficking (Confidence: {prediction_proba:.2%})")
    else:
        st.success(f"🟢 Low Risk of Human Trafficking (Confidence: {prediction_proba:.2%})")
