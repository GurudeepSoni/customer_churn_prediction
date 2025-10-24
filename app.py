import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
try:
    model = pickle.load(open('churn_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model or scaler file not found. Please ensure they are in the correct directory.")
    st.stop()

# Streamlit app title and description
st.title("📊 Customer Churn Prediction App 🚀")
st.write("Predict if a bank customer will leave the service using Machine Learning.")

st.header("🛠️ Enter Customer Details")

# User Inputs
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure (Years with bank)", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance ($)", min_value=0.0, value=50000.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox("Has Credit Card", ["Yes", "No"])
is_active_member = st.selectbox("Is Active Member", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary ($)", min_value=0.0, value=50000.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Process Inputs
gender = 1 if gender == "Male" else 0
has_cr_card = 1 if has_cr_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0

# Geography Encoding (drop_first=True was used, so only Germany and Spain columns are used)
geography_germany = 1 if geography == "Germany" else 0
geography_spain = 1 if geography == "Spain" else 0

# Create input array
input_data = np.array([[credit_score, gender, age, tenure, balance, num_of_products,
                        has_cr_card, is_active_member, estimated_salary,
                        geography_germany, geography_spain]])

# Prediction Button
if st.button("🎯 Predict Churn"):
    # Scale input
    input_scaled = scaler.transform(input_data)
    
    # Make Prediction
    prediction = model.predict(input_scaled)
    
    if prediction[0] == 1:
        st.error("❌ The customer is **likely to churn**.")
    else:
        st.success("✅ The customer is **not likely to churn**.")

# Footer
st.markdown("""
    <style>
    .watermark {
        color: #bbb;
        font-style: italic;
        opacity: 0.7;
        font-size: 14px;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="watermark">
        Created by Gurudeep Soni 💻
    </div>
""", unsafe_allow_html=True)
