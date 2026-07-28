import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(
    page_title="USA House Price Prediction",
    page_icon="🏠",
    layout="centered",
)


# LOAD MODEL
model_path = os.path.join(
    os.path.dirname(__file__),
    "Model",
    "house_price_model.pkl"
)

model = joblib.load(model_path)
scaler = joblib.load("Model/scaler.pkl")

# ADD TITLE
st.title("🏠 USA House Price Prediction ")
st.write(
    "Predict house prices using a Linear Regression model trained on the USA Housing dataset."
)
st.divider()


#  ADDING INPUT FEATURES
income = st.number_input(
    "💰 Average Area Income",
    min_value=17796.63,
    max_value=107701.75,
    value=68583.11
)

house_age = st.number_input(
    "🏡 Average Area House Age",
    min_value=2.64,
    max_value=9.52,
    value=5.98
)

rooms = st.number_input(
    "🛋️ Average Number of Rooms",
    min_value=3.24,
    max_value=10.76,
    value=6.99
)

bedrooms = st.number_input(
    "🛏️ Average Number of Bedrooms",
    min_value=2.0,
    max_value=6.5,
    value=3.98
)

population = st.number_input(
    "👨‍👩‍👧‍👦 Area Population",
    min_value=172.61,
    max_value=69621.71,
    value=36163.52
)


# CALCULATING THE EXTRA ADDED FEATURE
if  bedrooms!= 0:
    rooms_per_bedroom = rooms / bedrooms
else:
    rooms_per_bedroom = 0


if st.button("🔍 Predict Price"):
    features = np.array([[income,
                    house_age,
                    rooms,
                    bedrooms,                         
                    population,
                    rooms_per_bedroom]])

features_scaled = scaler.transform(features)
prediction = model.predict(features_scaled)[0]
if prediction < 0:
    st.error(
        "⚠️ The entered values result in an unrealistic prediction. "
        "Please use values closer to the training data distribution."
    )
else:
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")


st.divider()
st.subheader("📊 Model Performance")

st.write("**R² Score:** 0.9180")
st.write("**Mean Absolute Error (MAE):** $80,881.07")
st.write("**Root Mean Squared Error (RMSE):** $100,448.49")