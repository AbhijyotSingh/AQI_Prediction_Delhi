import pickle as pk
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Random_Forest.pk")

with open(model_path,"rb") as file:
    model=pk.load(file)
    
def predict(month,year,pm2_5,pm10,no2,so2,co,ozone):   
    data=np.array([[month,year,pm2_5,pm10,no2,so2,co,ozone]])
    predicted_aqi=model.predict(data)
    return predicted_aqi[0]

app=Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict_route():
    input_data=request.get_json()
    month=input_data["month"]
    year=input_data["year"]
    pm2_5=input_data["pm2_5"]
    pm10=input_data["pm10"]
    no2=input_data["no2"]
    so2=input_data["so2"]
    co=input_data["co"]
    ozone=input_data["ozone"]
    
    result=predict(month,year,pm2_5,pm10,no2,so2,co,ozone)
    
    return jsonify({"Predicted_AQI":float(result)})

if __name__=="__main__":
    app.run(debug=True)