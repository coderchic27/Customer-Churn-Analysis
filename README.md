📊 Customer Churn Prediction App

📌 Overview

This project predicts whether a customer will churn (leave) or stay using Machine Learning.

It includes:

- Data analysis (EDA)
- Model training
- Interactive web app

---

🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

📂 Project Structure

customer-churn-project/
│
├── app.py                  # Streamlit app
├── churn_model.pkl         # Trained ML model
├── churn_analysis.ipynb    # Jupyter notebook (EDA + training)
├── data/
│   └── churn.csv          # Dataset
├── requirements.txt
└── README.md

---

📊 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning Model (Random Forest)
- Interactive Dashboard using Streamlit
- Real-time Prediction

🧠 Model Details

- Algorithm: Random Forest Classifier
- Target Variable: Churn (0 = Stay, 1 = Leave)

---

📈 Model Performance

- Accuracy: ~78%
- Precision (Churn): 62%
- Recall (Churn): 46%

---

⚠️ Important Note

The current app uses limited input features (e.g., tenure and monthly charges).
Prediction accuracy can be improved by including more features from the dataset.

---

💡 Business Insights

- Customers with low tenure are more likely to churn
- Customers with higher monthly charges may churn
- Long-term customers are more likely to stay

---

🎯 Future Improvements

- Use full feature set for prediction
- Improve model accuracy
- Deploy app online (Streamlit Cloud / Render)
- Add better UI/UX

---
⭐ Acknowledgement

Dataset used for educational and project purposes.
