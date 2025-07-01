# 🧠 Global Mental Health Disorder Prediction

> Predicting the likelihood of mental health disorders across countries using machine learning and public health data.

---

## 🌍 Project Overview

This project aims to build a predictive model that identifies the likelihood of mental health disorders such as depression, anxiety, eating disorders, bipolar disorders and many more on a **global scale**, using demographic, socio-economic and health-related indicators.

The goal is to provide **data-driven insights** that can help global health organizations and policy makers target interventions where they are needed most.

---

## 🎯 Objectives

- 📊 Explore global mental health trends and indicators
- 🧠 Predict prevalence of mental disorders using ML models
- 🔍 Identify key risk factors contributing to mental health outcomes
- 🌐 Create a report for public awareness and policy advocacy

---

## 📁 Project Structure
mental-health-prediction/
│
├── 📂 data/
│ ├── raw/ # Original downloaded datasets
│ ├── processed/ # Cleaned & preprocessed data
│ └── external/ # WHO, World Bank, or CDC datasets
│
├── 📂 notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_model_training.ipynb
│ └── 04_evaluation_visuals.ipynb
│
├── 📂 models/
│ └── trained_model.pkl # Saved ML models
│
├── 📂 reports/
│ └── final_report.pdf # Summary findings, charts
│
├── 📂 src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── model.py
│ └── utils.py
│
├── requirements.txt # Python dependencies
├── README.md # Project overview
└── .gitignore

---

## 🧾 Datasets

- 🌐 [WHO World Mental Health Surveys](https://www.hcp.med.harvard.edu/wmh/)
- 🇺🇳 [Global Burden of Disease – Mental Health](https://ghdx.healthdata.org/gbd-results-tool)
- 🇺🇸 [CDC Mental Health Indicators](https://chronicdata.cdc.gov/)
- 💬 [Reddit Mental Health Dataset](https://www.kaggle.com/datasets/sbhatti/mental-health-in-social-media)

---

## 🛠️ Tools & Technologies

- **Languages:** Python (Pandas, NumPy)
- **ML Models:** Logistic Regression, Random Forest
- **Visualization:** Matplotlib, Seaborn, Plotly

---

## 📈 Project Flow

1. **Data Collection** – Merge datasets from multiple reliable sources
2. **Preprocessing** – Handle missing values, encode categorical data, normalize
3. **EDA** – Uncover trends by region, age, gender, income
4. **Modeling** – Train ML models to predict mental disorder risk
5. **Evaluation** – Use accuracy, ROC-AUC, F1-score
6. **Reporting** – Visualize trends and model insights in charts

---

## 🧠 Research Questions

- What socio-economic or environmental factors contribute to higher mental disorder prevalence globally?
- Can we predict regions most at risk of future mental health crises?
- How do mental health predictors vary across countries or demographics?

---

## 📌 Future Work

- Incorporate **time series** trends for forecasting
- Add **real-time social media** data for mood detection
- Develop a **global mental health dashboard** for public use

---

## 🙏 Acknowledgments

- World Health Organization (WHO)
- Institute for Health Metrics and Evaluation (IHME)
- CDC Public Health Datasets
- Kaggle and Reddit community datasets

---

## 📬 Contact

**Author:** Bethany Nyokabi  
**Project Advisor:** [Brayan Mwanyumba]  
📧 Email: bethanynyokabi@example.com  
---

