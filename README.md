# 🌱 Crop Recommendation System

## 📌 1. Introduction
Agriculture plays a vital role in food security and the economy. Choosing the right crop for a given soil type, climatic condition, and nutrient availability is crucial for sustainable farming.  

This project uses **Machine Learning (ML)** to build a Crop Recommendation System that suggests the most suitable crop based on soil nutrients and weather conditions.

---

## 📌 2. Problem Statement
Farmers often lack precise information about which crop will yield the best result under given environmental and soil conditions.  
Traditional methods rely on experience and manual observation, which may lead to poor crop selection.  

❓ The problem is: **Can we use AI/ML to recommend the best crop for given soil and weather conditions?**

---

## 📌 3. Objective
- Develop a classification model that predicts the most suitable crop.  
- Analyze soil & weather parameters that influence crop growth.  
- Build a simple system that can assist farmers in decision-making.  

---

## 📌 4. Dataset
- **Name:** Crop Recommendation Dataset (Kaggle)  
- **Attributes:**

| Feature      | Description |
|--------------|-------------|
| **N**        | Nitrogen content in soil |
| **P**        | Phosphorus content in soil |
| **K**        | Potassium content in soil |
| **temperature** | Average temperature (°C) |
| **humidity** | Humidity (%) |
| **pH**       | Acidity/alkalinity of soil |
| **rainfall** | Rainfall (mm) |
| **label**    | Crop name (Target Variable) |

- **Crops Covered:** 22  
*(rice, maize, chickpea, kidneybeans, pigeonpeas, mothbeans, mungbean, blackgram, lentil, pomegranate, banana, mango, grapes, watermelon, muskmelon, apple, orange, papaya, coconut, cotton, jute, coffee)*  

---

## 📌 5. Methodology
🔹 **Step 1 – Data Collection**  
- Dataset obtained from Kaggle.  

🔹 **Step 2 – Data Preprocessing**  
- Checked for missing values.  
- Converted data into features (X) and labels (y).  
- Train-test split applied (80%-20%).  

🔹 **Step 3 – Model Selection**  
- Used **Random Forest Classifier** because:  
  - Works well on tabular data.  
  - Handles multi-class classification.  
  - Provides feature importance.  

🔹 **Step 4 – Model Training**  
- Trained Random Forest with 100 decision trees.  

🔹 **Step 5 – Evaluation**  
- Evaluated using Accuracy Score and Classification Report (precision, recall, F1-score).  

🔹 **Step 6 – Prediction**  
- Tested with custom input → Recommended crop.  

---

## 📌 6. Tools & Libraries
- **Programming Language:** Python 3.x  

- **Libraries Used:**  
  - `pandas`, `numpy` → Data Handling  
  - `matplotlib`, `seaborn` → Visualization  
  - `scikit-learn` → Machine Learning Models  

---

## 📌 7. Results
- Achieved **>95% accuracy** on test data.  
- Model successfully predicts suitable crops based on input conditions.  

---


---

## 📌 8. Applications
- Helps farmers decide the best crop for their land.  
- Reduces risk of crop failure.  
- Promotes sustainable agriculture by optimizing soil usage.  

---

## 📌 9. Future Enhancements
- Add real-time weather API for live predictions.  
- Build a **Streamlit web app** with user input form.  
- Extend to **pest/disease prediction** with image data.  
- Deploy model as a **mobile app** for farmer-friendly usage.  

---

## 📌 10. Conclusion
This project demonstrates how **AI/ML can assist in sustainable agriculture** by recommending crops based on soil and climate data.  
The model is simple yet effective and can be integrated into decision support systems for smart farming.  
