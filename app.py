from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel


model=joblib.load("ChurnModel.pkl")

app=FastAPI()


class Inputdata(BaseModel):
    CreditScore:int
    Geography:str
    Gender:str
    Age:int
    Tenure:int
    Balance:float
    NumOfProducts:int
    IsActiveMember:int


@app.get("/")

def home():
    return "Fast API Is Runing."

@app.post("/predict")

def predict(data:Inputdata):

    input_data=pd.DataFrame([{

        "CreditScore": data.CreditScore,
        "Geography": data.Geography,
        "Gender": data.Gender,
        "Age": data.Age,
        "Tenure": data.Tenure,
        "Balance": data.Balance,
        "NumOfProducts": data.NumOfProducts,
        "IsActiveMember": data.IsActiveMember
 }])


    predict = int(model.predict(input_data)[0])

    prob = float(model.predict_proba(input_data)[0][1])

    prediction = 1 if prob > 0.35 else 0

    if prob < 0.3:
        risk = "Low Risk"
    elif prob < 0.7:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    return {
        "Churn Probability": prob,
        "prediction": prediction,
        "risk": risk
    }



