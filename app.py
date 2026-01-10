import streamlit as st
import requests

# ===============================
# BACKEND CONFIG (IMPORTANT)
# ===============================
# Replace with your EC2 Public IP
BACKEND_URL = "http://51.21.182.215:8000"

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Aviation Delay Predictor",
    layout="centered"
)

st.title("✈️ Aviation Flight Delay Predictor")
st.caption("Flight delay prediction using ML + FastAPI")
st.divider()

# ===============================
# INPUT SECTION
# ===============================
st.subheader("🧾 Flight Details")

airline = st.selectbox(
    "Airline",
    ["Indigo", "Vistara", "Air India", "Akasa Air", "SpiceJet"]
)

source = st.selectbox(
    "Source City",
    ["Mumbai", "Delhi", "Pune", "Kolkata", "Chennai", "Hyderabad", "Kochi"]
)

destination = st.selectbox(
    "Destination City",
    ["Mumbai", "Delhi", "Pune", "Kolkata", "Chennai", "Hyderabad", "Kochi"]
)

weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Rain", "Fog", "Thunderstorm"]
)

traffic = st.selectbox(
    "Airport Traffic",
    ["Low", "Medium"]
)

# ===============================
# ONE-HOT ENCODE INPUT
# ===============================
input_data = {
    # Airline
    "Airline_Indigo": airline == "Indigo",
    "Airline_Vistara": airline == "Vistara",
    "Airline_Air India": airline == "Air India",
    "Airline_Akasa Air": airline == "Akasa Air",
    "Airline_SpiceJet": airline == "SpiceJet",

    # Source
    "Source_Mumbai": source == "Mumbai",
    "Source_Delhi": source == "Delhi",
    "Source_Pune": source == "Pune",
    "Source_Kolkata": source == "Kolkata",
    "Source_Chennai": source == "Chennai",
    "Source_Hyderabad": source == "Hyderabad",
    "Source_Kochi": source == "Kochi",

    # Destination
    "Destination_Mumbai": destination == "Mumbai",
    "Destination_Delhi": destination == "Delhi",
    "Destination_Pune": destination == "Pune",
    "Destination_Kolkata": destination == "Kolkata",
    "Destination_Chennai": destination == "Chennai",
    "Destination_Hyderabad": destination == "Hyderabad",
    "Destination_Kochi": destination == "Kochi",

    # Weather
    "Weather_Rain": weather == "Rain",
    "Weather_Fog": weather == "Fog",
    "Weather_Thunderstorm": weather == "Thunderstorm",

    # Traffic
    "Airport Traffic_Low": traffic == "Low",
    "Airport Traffic_Medium": traffic == "Medium",
}

# ===============================
# PREDICTION BUTTON
# ===============================
if st.button("🚀 Predict Delay"):
    try:
        # ---- Prediction API ----
        pred_response = requests.post(
            f"{BACKEND_URL}/tool/predict-flight-delay",
            json=input_data,
            timeout=5
        )
        prediction = pred_response.json()["prediction"]

        st.success(f"⏱️ Predicted Delay: {prediction} minutes")

        # ---- Risk Level ----
        if prediction >= 10:
            st.error("🔴 High Delay Risk")
        elif prediction >= 5:
            st.warning("🟡 Medium Delay Risk")
        else:
            st.success("🟢 Low Delay Risk")

        # ---- Reasoning API ----
        reason_response = requests.post(
            f"{BACKEND_URL}/tool/delay-reason",
            json=input_data,
            timeout=5
        )
        reasons = reason_response.json()["reasons"]

        st.divider()
        st.subheader("🧠 Why this delay?")
        for r in reasons:
            st.write("•", r)

    except Exception as e:
        st.error("❌ Backend not reachable. Make sure FastAPI is running on port 8000.")
