const ML_SERVICE_URL = process.env.ML_SERVICE_URL || "http://localhost:5001";

const callMlService = async (endpoint, payload) => {
  const response = await fetch(`${ML_SERVICE_URL}${endpoint}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message || "ML prediction service error");
  }

  return data;
};

const predictDiabetes = async (req, res) => {
  try {
    const data = await callMlService("/predict/diabetes", req.body);

    res.json({
      success: true,
      data,
    });
  } catch (error) {
    console.error("Diabetes prediction error:", error.message);

    res.status(500).json({
      success: false,
      message: error.message || "Diabetes prediction failed",
    });
  }
};

const predictHeart = async (req, res) => {
  try {
    const data = await callMlService("/predict/heart", req.body);

    res.json({
      success: true,
      data,
    });
  } catch (error) {
    console.error("Heart prediction error:", error.message);

    res.status(500).json({
      success: false,
      message: error.message || "Heart disease prediction failed",
    });
  }
};

export { predictDiabetes, predictHeart };
