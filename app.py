import streamlit as st
import numpy as np
import pickle

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Predictor")

overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Above ground living area (sq ft)", 500, 5000, 1500)
garage_cars = st.slider("Garage Capacity (Cars)", 0, 4, 2)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
full_bath = st.slider("Number of Full Bathrooms", 0, 4, 2)

input_data = np.array([[overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, full_bath]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
