from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]

        # Prediction
        prediction = model.predict(final_features)

        # Confidence score
        probability = model.predict_proba(final_features)
        confidence = round(max(probability[0]) * 100, 2)

        # Result text
        if prediction[0] == 1:
            result = f"High Risk of Heart Disease ({confidence}% Confidence)"
        else:
            result = f"Low Risk of Heart Disease ({confidence}% Confidence)"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text="Error: Please enter valid input values.")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)