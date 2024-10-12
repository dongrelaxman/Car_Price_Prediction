# Car Price Prediction App
Welcome to the Car Price Prediction App! This project leverages a machine learning model to predict the price of a car based on its model year and mileage. The app is built using Streamlit for the user interface and scikit-learn for the machine learning pipeline.

## Features

**Predict Car Prices:** Users can input the car's model year and mileage, and the app will predict the car's price based on a trained machine learning model.

**User-Friendly Interface:** The app is built using Streamlit, providing an intuitive interface for users to input data and get predictions.

**Model Deployment Button:** Simulate the deployment of the machine learning model by triggering the "Deploy Model" button.

# Demo
## Prediction Interface:
![alt text](<Screenshot 2024-10-05 100049.png>)

Installation and Setup
To run this project locally, follow these steps:

Clone the repository:
`git clone https://github.com/your-username/car-price-prediction-app.git`
`cd car-price-prediction-app`

**Install dependencies:** Ensure you have Python 3.7+ installed. 

**Install required Python packages using:**

`pip install -r requirements.txt`

Prepare the machine learning model: If you don't have a pre-trained model, train one by running your model training script or download the pre-trained model car_price_model1.pkl from the repository.

## Run the Streamlit App: 
Start the Streamlit app with the following command:
`streamlit run app.py`
Visit the app: Open the app in your browser at `http://localhost:8501.`

## How to Use

Select a Model Year from the dropdown menu.
Input the Mileage of the car.
Click the **"Predict Price"** button to get the car's estimated price.

**Model Training**

The machine learning model was trained using a Linear Regression algorithm. Here's a brief overview of the model training process:

Data Preprocessing: Categorical features were one-hot encoded using OneHotEncoder, and a pipeline was created to preprocess data and fit the model.
Metrics: The model's performance was evaluated using the Root Mean Squared Error (RMSE) and R-squared (R²) score.
To retrain the model, refer to the train_model.py file and follow the instructions inside.

Contributing
We welcome contributions to this project! Here’s how you can contribute:

Fork the repository.
Clone your fork:
bash
Copy code
git clone https://github.com/your-username/car-price-prediction-app.git
Make your changes.
Submit a pull request and we’ll review your changes!
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
For any inquiries or issues, feel free to reach out via dongrei481@gmail.com

