# 🏡 Jaipur Real Estate Price Prediction & Analytics System

This project is an end-to-end data science application that analyzes real estate data from Jaipur and provides price prediction, insights, and analytics through an interactive web interface built with Streamlit.

The goal of this project is to help users understand property pricing patterns and explore how different features affect the overall price.

---

## 🚀 Key Features

### 📊 Analytics Module
- Visual analysis of property prices across different locations
- Price distribution and trend analysis
- Area vs price relationship
- BHK-wise and feature-based comparisons

### 💰 Price Prediction Module
- Predicts property price based on user inputs
- Uses trained machine learning pipelines
- Supports multiple property types such as flats, builder floors, houses, villas, and plots

### 🔍 Recommendation Module
- Suggests similar properties based on selected inputs
- Helps users explore comparable options

### 💡 Insights Module
- Provides interactive "what-if" analysis
- Shows how changing features (BHK, area, etc.) impacts price
- Explains price changes with simple reasoning and suggestions

---

## 🧠 Machine Learning Approach

- Data collected from multiple sources (flats, independent houses, plots)
- Data preprocessing included:
  - Missing value handling
  - Outlier removal
  - Feature engineering
- Models experimented:
  - Linear Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
- Final model selected based on performance (R² and MAE)

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Visualization:** Plotly
- **Frontend:** Streamlit  

---

## 📁 Project Structure
Jaipur-Real-Estate-Capstone-project/

│

├── App/

│ ├── home.py # Main entry point (Streamlit home page)

│ │

│ ├── pages/

│ │ ├── Analytics.py # Analytics module

│ │ ├── Prediction.py # Price prediction module

│ │ ├── Recommendation.py # Recommendation system

│ │ ├── Insights.py # What-if analysis module

│ │

│ ├── data/ # Dataset used in the application

