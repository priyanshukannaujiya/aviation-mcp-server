from fastapi import FastAPI
import pandas as pd
import joblib

# ----------------------------------
# Load trained ML model
# ----------------------------------
model = joblib.load("model.pkl")

# Feature order used during training
FEATURES = list(model.feature_names_in_)

app = FastAPI(title="Aviation MCP-style Server")

# ----------------------------------
# TOOL 1: Prediction (ML + Business Rules)
# ----------------------------------
@app.post("/tool/predict-flight-delay")
def predict_flight_delay(input_data: dict):
    """
    Predict flight delay using ML model
    + real-world business rules
    """

    # Convert input to DataFrame
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=FEATURES, fill_value=0)

    # Base ML prediction
    prediction = int(model.predict(df)[0])

    # -----------------------------
    # Business Rule Adjustments
    # -----------------------------
    if input_data.get("Weather_Thunderstorm", 0) == 1:
        prediction += 7

    if input_data.get("Weather_Rain", 0) == 1:
        prediction += 3

    if input_data.get("Weather_Fog", 0) == 1:
        prediction += 4

    if input_data.get("Airport Traffic_Medium", 0) == 1:
        prediction += 3

    # Safety clamp
    if prediction < 0:
        prediction = 0

    return {
        "prediction": prediction
    }


# ----------------------------------
# TOOL 2: Reasoning (WHY this delay)
# ----------------------------------
@app.post("/tool/delay-reason")
def delay_reason(input_data: dict):
    """
    Explain WHY the delay risk is high / medium / low
    """

    reasons = []

    # Weather reasoning
    if input_data.get("Weather_Thunderstorm", 0) == 1:
        reasons.append("Thunderstorm significantly disrupts flight operations")

    if input_data.get("Weather_Rain", 0) == 1:
        reasons.append("Rain slows down runway and ground handling")

    if input_data.get("Weather_Fog", 0) == 1:
        reasons.append("Fog reduces visibility and increases spacing between flights")

    # Airport traffic reasoning
    if input_data.get("Airport Traffic_Medium", 0) == 1:
        reasons.append("Moderate airport traffic can cause congestion delays")

    if input_data.get("Airport Traffic_Low", 0) == 1:
        reasons.append("Low airport traffic helps flights stay on time")

    # Fallback
    if not reasons:
        reasons.append("Normal operating conditions detected")

    return {
        "reasons": reasons
    }
