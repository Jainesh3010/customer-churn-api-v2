# 🚀 Customer Churn Prediction API

A production-ready Machine Learning API that predicts customer churn probability and classifies customers into risk categories using XGBoost and FastAPI.

## 🌐 Live Demo

**API URL:**
https://customer-churn-prediction-fastapi-vz3m.onrender.com

**Swagger Documentation:**
https://customer-churn-prediction-fastapi-vz3m.onrender.com/docs

---

## 📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses and banks. This project predicts whether a customer is likely to leave the company based on customer demographics and account information.

The model is deployed as a REST API using FastAPI and can provide real-time predictions.

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* FastAPI
* Joblib
* Uvicorn
* Render (Cloud Deployment)

---

## 📊 Model Performance

| Metric   | Score |
| -------- | ----- |
| ROC-AUC  | 0.87  |
| Recall   | 0.63  |
| F1 Score | 0.61  |
| Log Loss | 0.32  |

---

## 📥 Input Features

| Feature         |
| --------------- |
| CreditScore     |
| Geography       |
| Gender          |
| Age             |
| Tenure          |
| Balance         |
| NumOfProducts   |
| IsActiveMember  |
| EstimatedSalary |

---

## 🔮 API Endpoint

### POST /predict

### Sample Request

```json
{
  "CreditScore": 620,
  "Geography": "Germany",
  "Gender": "Female",
  "Age": 48,
  "Tenure": 2,
  "Balance": 125000,
  "NumOfProducts": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 85000
}
```

### Sample Response

```json
{
  "churn_probability": 0.87,
  "prediction": 1,
  "risk_level": "High Risk"
}
```

---

## ⚙️ Run Locally

```bash
git clone <repository-url>

cd customer-churn-prediction-fastapi

pip install -r requirement.txt

uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 📈 Business Value

* Identify high-risk customers
* Improve customer retention strategies
* Enable proactive customer engagement
* Reduce revenue loss due to churn

---

## 📷 Project Screenshots

Add:

* FastAPI Swagger UI Screenshot
* Prediction Output Screenshot
* Model Evaluation Screenshot

---

## 👨‍💻 Author

**Jainesh Sanghavi**

Machine Learning | Data Science | Deep Learning Enthusiast

---

### ⭐ If you found this project useful, consider giving it a star.
