import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction App")

tenure = st.slider("Tenure", 0, 72)
monthly_charges = st.number_input("Monthly Charges")

if st.button("Predict"):
    input_data = np.zeros((1, 30))
    input_data[0][1] = tenure
    input_data[0][2] = monthly_charges

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")