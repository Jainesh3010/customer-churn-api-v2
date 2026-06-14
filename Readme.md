# 🚀 Customer Churn Analytics & Prediction System

An end-to-end Data Science project that combines Data Analysis, SQL, Power BI, Machine Learning, FastAPI, and Cloud Deployment to predict customer churn and identify high-risk customers.

---

## 🌐 Live API

**API Endpoint**

https://customer-churn-prediction-fastapi-vz3m.onrender.com

**Swagger Documentation**

https://customer-churn-prediction-fastapi-vz3m.onrender.com/docs

---

## 📌 Project Overview

Customer churn is a critical business problem where customers stop using a company's services. This project analyzes customer behavior, identifies churn patterns, and predicts whether a customer is likely to churn.

The complete solution includes:

* Exploratory Data Analysis (EDA)
* SQL-based Business Analysis
* Power BI Dashboard
* Machine Learning Model
* FastAPI REST API
* Cloud Deployment on Render

---

## 🛠️ Tech Stack

### Data Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### Database

* SQL

### Visualization

* Power BI

### Machine Learning

* Scikit-Learn
* XGBoost

### Deployment

* FastAPI
* Uvicorn
* Render

---

## 📊 Data Analysis

The dataset was analyzed to understand customer behavior and identify factors influencing churn.

### Analysis Performed

* Customer Demographics Analysis
* Churn Distribution Analysis
* Geography-wise Churn Analysis
* Gender-wise Analysis
* Age vs Churn Analysis
* Balance vs Churn Analysis
* Product Usage Analysis
* Active Member Analysis
* Tenure Analysis

### Key Insights

* Inactive customers showed higher churn rates.
* Customers with fewer products were more likely to churn.
* Customer age significantly influenced churn behavior.
* Geography played an important role in churn patterns.
* Tenure and account balance impacted customer retention.

---

## 📈 Power BI Dashboard

An interactive dashboard was created to visualize:

* Total Customers
* Churn Rate
* Customer Segmentation
* Geography Analysis
* Age Distribution
* Product Analysis
* Customer Activity Trends

---

## 🤖 Machine Learning Model

### Model Used

* XGBoost Classifier

### Input Features

* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* IsActiveMember

### Model Performance

| Metric   | Score |
| -------- | ----- |
| ROC-AUC  | 0.87  |
| Recall   | 0.63  |
| F1 Score | 0.61  |
| Log Loss | 0.32  |

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
  "IsActiveMember": 0
}
```

### Sample Response

```json
{
  "Churn Probability": 0.87,
  "Prediction": 1,
  "risk": "High Risk"
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

## 📁 Project Structure

```text
├── Data
├── Notebooks
├── SQL
├── Power BI Report
├── Screenshots
├── app.py
├── ChurnModel.pkl
├── requirement.txt
└── README.md
```

---

## 💼 Business Impact

This system can help organizations:

* Identify customers likely to churn
* Improve retention strategies
* Reduce customer loss
* Enable targeted marketing campaigns
* Improve customer lifetime value

---

## 📷 Screenshots
<img width="1050" height="932" alt="6e13a83f-cfbf-46b8-b269-c0858c951c7c" src="https://github.com/user-attachments/assets/a6cfd939-3b38-4fcf-b094-bf66341de072" />


<img width="1055" height="929" alt="c1264ad0-43de-46d1-9cd9-fee2602e7c43" src="https://github.com/user-attachments/assets/7eb68121-12af-4a02-af34-998d4eb075b9" />


<img width="1048" height="580" alt="234fcb91-7f44-4b23-a7a5-1c959e836a8c" src="https://github.com/user-attachments/assets/53cad52f-0819-4815-913e-bcb3a0a485c5" />


<img width="1033" height="1023" alt="Screenshot 2026-06-14 151819" src="https://github.com/user-attachments/assets/bcc27e3e-6d12-4ec2-bbdb-0741ba332d00" />



---

## 👨‍💻 Author

**Jainesh Sanghavi**

Data Science | Machine Learning | Deep Learning

GitHub: https://github.com/Jainesh3010

---

⭐ If you found this project useful, please consider giving it a star.
