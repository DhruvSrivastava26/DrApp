import os
import joblib
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

diabetes_model = joblib.load(os.path.join(MODEL_DIR, "diabetes_model.pkl"))
diabetes_scaler = joblib.load(os.path.join(MODEL_DIR, "diabetes_scaler.pkl"))
heart_model = joblib.load(os.path.join(MODEL_DIR, "heart_model.pkl"))

app = Flask(__name__)
CORS(app)


@app.get("/")
def home():
    return jsonify({
        "success": True,
        "message": "ML prediction service is running"
    })


@app.post("/predict/diabetes")
def predict_diabetes():
    try:
        data = request.get_json()

        required_fields = [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age"
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "success": False,
                "message": f"Missing fields: {', '.join(missing_fields)}"
            }), 400

        input_data = [
            float(data["Pregnancies"]),
            float(data["Glucose"]),
            float(data["BloodPressure"]),
            float(data["SkinThickness"]),
            float(data["Insulin"]),
            float(data["BMI"]),
            float(data["DiabetesPedigreeFunction"]),
            float(data["Age"])
        ]

        input_array = np.asarray(input_data).reshape(1, -1)
        scaled_input = diabetes_scaler.transform(input_array)

        prediction = diabetes_model.predict(scaled_input)[0]

        if int(prediction) == 1:
            result = "The person may have diabetes risk"
            risk = "high"
        else:
            result = "The person may not have diabetes risk"
            risk = "low"

        return jsonify({
            "success": True,
            "prediction": int(prediction),
            "risk": risk,
            "result": result,
            "disclaimer": "This prediction is informational only and not a medical diagnosis."
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@app.post("/predict/heart")
def predict_heart():
    try:
        data = request.get_json()

        required_fields = [
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal"
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "success": False,
                "message": f"Missing fields: {', '.join(missing_fields)}"
            }), 400

        input_data = [
            float(data["age"]),
            float(data["sex"]),
            float(data["cp"]),
            float(data["trestbps"]),
            float(data["chol"]),
            float(data["fbs"]),
            float(data["restecg"]),
            float(data["thalach"]),
            float(data["exang"]),
            float(data["oldpeak"]),
            float(data["slope"]),
            float(data["ca"]),
            float(data["thal"])
        ]

        input_array = np.asarray(input_data).reshape(1, -1)

        prediction = heart_model.predict(input_array)[0]

        if int(prediction) == 1:
            result = "The person may have heart disease risk"
            risk = "high"
        else:
            result = "The person may not have heart disease risk"
            risk = "low"

        return jsonify({
            "success": True,
            "prediction": int(prediction),
            "risk": risk,
            "result": result,
            "disclaimer": "This prediction is informational only and not a medical diagnosis."
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
