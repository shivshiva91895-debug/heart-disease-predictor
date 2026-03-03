import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

print("Enter Patient Details:")

features = []
features.append(float(input("Age: ")))
features.append(float(input("Sex (1=Male, 0=Female): ")))
features.append(float(input("Chest Pain Type (0-3): ")))
features.append(float(input("Resting BP: ")))
features.append(float(input("Cholesterol: ")))
features.append(float(input("Fasting Blood Sugar (0/1): ")))
features.append(float(input("Rest ECG (0-2): ")))
features.append(float(input("Max Heart Rate: ")))
features.append(float(input("Exercise Induced Angina (0/1): ")))
features.append(float(input("Oldpeak: ")))
features.append(float(input("Slope (0-2): ")))
features.append(float(input("CA (0-3): ")))
features.append(float(input("Thal (0-3): ")))

prediction = model.predict([features])

if prediction[0] == 1:
    print("High Risk of Heart Disease")
else:
    print("Low Risk of Heart Disease")