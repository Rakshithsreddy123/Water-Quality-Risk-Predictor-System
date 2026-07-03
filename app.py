from flask import Flask, render_template, request
from src.evaluate import evaluate_rules
import numpy as np
import pickle

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

feature_order = [
    'pH', 'Hardness', 'Solids', 'Chloramines', 'Sulfate',
    'Conductivity', 'Organic_carbon', 'Trihalomethanes',
    'Turbidity'
]

PRESET_VALUES = {
    "pH": [7,8.7,9.5],
    "Hardness": [150,350,500],
    "Solids": [300,800,1500],
    "Chloramines": [2,4,7],
    "Sulfate": [200,300,500],
    "Conductivity": [200,400,800],
    "Organic_carbon": [1,2.5,5],
    "Trihalomethanes": [50,80,120],
    "Turbidity": [3,7,15]
}

def predict_water_quality(data):
    risk, triggered = evaluate_rules(data)

    if risk == "High Risk":
        status = "Unsafe"
    else:
        input_data = np.array([[data[f] for f in feature_order]])
        scaled_data = scaler.transform(input_data)
        pred = model.predict(scaled_data)[0]
        status = "Safe" if pred == 1 else "Unsafe"

    reasons = []
    suggestions = []

    for item in triggered:
        reasons.append(f"{item['parameter']}: {item['reason']}")
        suggestions.extend(item['suggestions'])

    if not reasons:
        reasons.append("All parameters are within acceptable limits")
        suggestions.append("Water is safe for drinking")

    return {
        "status": status,
        "risk": risk,
        "reasons": list(set(reasons)),
        "suggestions": list(set(suggestions))
    }



# 🔷 Input Page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", presets=PRESET_VALUES)


# 🔷 Result Page
@app.route("/result", methods=["POST"])
def result():

    data = {}

    for feature in feature_order:
        data[feature] = float(request.form.get(feature))

    result = predict_water_quality(data)

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)