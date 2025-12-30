import streamlit as st
import requests

# ---------------------------------
# Page config
# ---------------------------------
st.set_page_config(
    page_title="Aviation Delay Predictor",
    layout="centered"
)

st.title("✈️ Aviation Flight Delay Predictor")
st.caption("MCP-style: Prediction + Reasoning")

st.divider()

# ---------------------------------
# INPUT SECTION
# ---------------------------------
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

st.divider()

# ---------------------------------
# ONE-HOT ENCODING (MATCH MODEL)
# ---------------------------------
input_data = {
    # Airline
    "Airline_Indigo": 1 if airline == "Indigo" else 0,
    "Airline_Vistara": 1 if airline == "Vistara" else 0,
    "Airline_Air India": 1 if airline == "Air India" else 0,
    "Airline_Akasa Air": 1 if airline == "Akasa Air" else 0,
    "Airline_SpiceJet": 1 if airline == "SpiceJet" else 0,

    # Source
    "Source_Mumbai": 1 if source == "Mumbai" else 0,
    "Source_Delhi": 1 if source == "Delhi" else 0,
    "Source_Pune": 1 if source == "Pune" else 0,
    "Source_Kolkata": 1 if source == "Kolkata" else 0,
    "Source_Chennai": 1 if source == "Chennai" else 0,
    "Source_Hyderabad": 1 if source == "Hyderabad" else 0,
    "Source_Kochi": 1 if source == "Kochi" else 0,

    # Destination
    "Destination_Mumbai": 1 if destination == "Mumbai" else 0,
    "Destination_Delhi": 1 if destination == "Delhi" else 0,
    "Destination_Pune": 1 if destination == "Pune" else 0,
    "Destination_Kolkata": 1 if destination == "Kolkata" else 0,
    "Destination_Chennai": 1 if destination == "Chennai" else 0,
    "Destination_Hyderabad": 1 if destination == "Hyderabad" else 0,
    "Destination_Kochi": 1 if destination == "Kochi" else 0,

    # Weather
    "Weather_Rain": 1 if weather == "Rain" else 0,
    "Weather_Fog": 1 if weather == "Fog" else 0,
    "Weather_Thunderstorm": 1 if weather == "Thunderstorm" else 0,

    # Airport Traffic
    "Airport Traffic_Low": 1 if traffic == "Low" else 0,
    "Airport Traffic_Medium": 1 if traffic == "Medium" else 0,
}

# ---------------------------------
# PREDICT BUTTON
# ---------------------------------
if st.button("🚀 Predict Delay"):
    try:
        # ---- Prediction Tool ----
        pred_res = requests.post(
            "http://127.0.0.1:8000/tool/predict-flight-delay",
            json=input_data
        )
        prediction = pred_res.json()["prediction"]

        st.success(f"⏱️ Predicted Delay: {prediction} minutes")

        # ---- Risk Classification ----
        if prediction >= 10:
            st.error("🔴 High Delay Risk")
        elif prediction >= 5:
            st.warning("🟡 Medium Delay Risk")
        else:
            st.success("🟢 Low Delay Risk")

        # ---- Reasoning Tool ----
        reason_res = requests.post(
            "http://127.0.0.1:8000/tool/delay-reason",
            json=input_data
        )

        reasons = reason_res.json()["reasons"]

        st.divider()
        st.subheader("🧠 Why this delay?")
        for r in reasons:
            st.write("•", r)

    except Exception as e:
        st.error("Backend server not running. Start FastAPI first.")
