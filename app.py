import streamlit as st
import pandas as pd
import joblib
import json

# -----------------------------
# Load model and features
# -----------------------------

model = joblib.load("models/app_model.pkl")

with open("models/app_features.json", "r") as f:
    selected_features = json.load(f)


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Tablet Disintegration Predictor",
    page_icon="💊",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("💊 Tablet Disintegration Time Predictor")

st.write(
    "Enter the tablet formulation and physical properties "
    "to estimate the disintegration time."
)

st.divider()


# -----------------------------
# Input fields
# -----------------------------

wetting_time = st.number_input(
    "Wetting Time",
    min_value=0.0,
    max_value=369.0,
    value=34.23,
    step=0.01
)

hardness = st.number_input(
    "Hardness",
    min_value=0.81,
    max_value=21.67,
    value=3.56,
    step=0.01
)

thickness = st.number_input(
    "Thickness",
    min_value=0.0,
    max_value=10.89,
    value=2.33,
    step=0.01
)

mannitol = st.number_input(
    "Mannitol",
    min_value=0.0,
    max_value=410.55,
    value=49.86,
    step=0.01
)

friability = st.number_input(
    "Friability",
    min_value=0.0,
    max_value=27.17,
    value=0.55,
    step=0.01
)

topological_surface_area = st.number_input(
    "Topological Surface Area",
    min_value=3.20,
    max_value=304.0,
    value=93.36,
    step=0.01
)

microcrystalline_cellulose = st.number_input(
    "Microcrystalline Cellulose",
    min_value=0.0,
    max_value=397.40,
    value=57.92,
    step=0.01
)

magnesium_stearate = st.number_input(
    "Magnesium Stearate",
    min_value=0.0,
    max_value=30.0,
    value=2.43,
    step=0.01
)

xlogp3_aa = st.number_input(
    "XLogP3-AA",
    min_value=-2.90,
    max_value=7.86,
    value=2.70,
    step=0.01
)

logs = st.number_input(
    "LogS",
    min_value=-10.05,
    max_value=-0.44,
    value=-4.04,
    step=0.01
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Disintegration Time"):

    input_data = pd.DataFrame([[
        wetting_time,
        hardness,
        thickness,
        mannitol,
        friability,
        topological_surface_area,
        microcrystalline_cellulose,
        magnesium_stearate,
        xlogp3_aa,
        logs
    ]], columns=selected_features)

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Disintegration Time: {prediction:.2f}"
    )