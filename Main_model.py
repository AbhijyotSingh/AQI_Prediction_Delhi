import pickle as pk
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Random_Forest.pk")
scaler_path=os.path.join(BASE_DIR,"scaler.pk")

with open(model_path,"rb") as file:
    model=pk.load(file)

with open(scaler_path,"rb") as file:
    scaler=pk.load(file)
    
def predict(month,year,pm2_5,pm10,no2,so2,co,ozone):   
    data=np.array([[month,year,pm2_5,pm10,no2,so2,co,ozone]])
    data_scaled=scaler.transform(data)
    predicted_aqi=model.predict(data_scaled)
    return predicted_aqi[0]

app=Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict_route():
    input_data=request.get_json()
    month=float(input_data["month"])
    year=float(input_data["year"])
    pm2_5=float(input_data["pm2_5"])
    pm10=float(input_data["pm10"])
    no2=float(input_data["no2"])
    so2=float(input_data["so2"])
    co=float(input_data["co"])
    ozone=float(input_data["ozone"])
    
    result=predict(month,year,pm2_5,pm10,no2,so2,co,ozone)
    
    return jsonify({"Predicted_AQI":float(result)})

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
