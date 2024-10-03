import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('car_price_model1.pkl')

# Sample data for dropdown options
data_samples = [
    {"model_year": 2007, "milage": 213000},
    {"model_year": 2002, "milage": 143250},
    {"model_year": 2002, "milage": 136731},
    {"model_year": 2017, "milage": 19500},
    {"model_year": 2021, "milage": 7388},
]

# Create lists for dropdowns based on the sample data
model_years = list(set(sample['model_year'] for sample in data_samples))
milages = list(set(sample['milage'] for sample in data_samples))

# UI for inputs
st.title("Car Price Prediction")
st.header("Select Car Features")

model_year = st.selectbox('Model Year', model_years)
milage = st.number_input('Milage (in miles)', min_value=0, value=0)

# Create input DataFrame
input_data = {
    "model_year": model_year,
    "milage": milage,
}

input_df = pd.DataFrame([input_data])

# Predict price on button click
if st.button('Predict Price'):
    prediction = model.predict(input_df)
    st.write(f"Predicted Price: ${prediction[0]:,.2f}")

# Deploy button
if st.button('Deploy Model'):
    # Here you could add logic to deploy the model (e.g., save it to a cloud service)
    st.write("Model deployment logic goes here!")
