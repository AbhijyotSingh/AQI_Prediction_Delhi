import pickle as pk
import numpy as np

#Loading the model

with open(r"Projects\AQI - Regression\Random_Forest.pk","rb") as file:
    model=pk.load(file)
    
try:
    month=int(input("Enter month in integer: "))
    if month<1 or month>12:
        print("Please enter month between 1-12")
        exit()
    else:
        year=int(input("Enter year: "))
        pm2_5=float(input("Enter Particulate Matter < 2.5 micrometers in ug/m^3: "))
        pm10=float(input("Enter Particulate Matter < 10 micrometers in ug/m^3: "))
        no2=float(input("Enter the quantity of Nitrogen Dioxide (NO2) in ug/m^3: "))
        so2=float(input("Enter Sulphur Dioxde in in ug/m^3: "))
        co=float(input("Enter Carbon Monoxide in in ug/m^3: "))
        ozone=float(input("Enter quantity of Ozone in ug/m^3: "))

except ValueError:
    print("Exception occured: Value Error")
    exit()

else:
    data=np.array([[month,year,pm2_5,pm10,no2,so2,co,ozone]])
    predicted_aqi=model.predict(data)
    print("Predicted AQI for the given data is:",predicted_aqi[0])