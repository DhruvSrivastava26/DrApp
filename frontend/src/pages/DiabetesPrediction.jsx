import { useState } from "react";
import axios from "axios";

const DiabetesPrediction = () => {
  const [formData, setFormData] = useState({
    Pregnancies: "",
    Glucose: "",
    BloodPressure: "",
    SkinThickness: "",
    Insulin: "",
    BMI: "",
    DiabetesPedigreeFunction: "",
    Age: ""
  });

  const [result, setResult] = useState(null);

  const token = localStorage.getItem("token");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        "http://localhost:4000/api/predict/diabetes",
        formData,
        {
          headers: { token }
        }
      );

      setResult(res.data.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Diabetes Prediction</h1>

      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
        {Object.keys(formData).map((key) => (
          <input
            key={key}
            type="number"
            name={key}
            placeholder={key}
            value={formData[key]}
            onChange={handleChange}
            className="border p-2 rounded"
            required
          />
        ))}
        <button className="col-span-2 bg-blue-500 text-white p-2 rounded">
          Predict
        </button>
      </form>

      {result && (
        <div className="mt-6 p-4 border rounded">
          <h2 className="text-lg font-semibold">{result.result}</h2>
          <p className={result.risk === "high" ? "text-red-500" : "text-green-500"}>
            Risk: {result.risk}
          </p>
        </div>
      )}
    </div>
  );
};

export default DiabetesPrediction;