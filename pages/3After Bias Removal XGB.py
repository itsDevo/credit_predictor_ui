import streamlit as st
import pickle
import pandas as pd
from utils import model_c

st.set_page_config(page_title="Credit Score Predictor",layout="wide")

st.markdown("<h1 style='text-align: center;'>Credit Score Predictor (After Bias Removal) (XGBoost)</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August"])
    city = st.selectbox("City", ['None'],help="This feature is not used in this model",disabled=True) # All cities in the dataset is included
    age = st.number_input("Age", min_value=18, max_value=100,help="Represents the age of the person",disabled=True)
    occupation = st.selectbox("Occupation", ['Architect', 'Cleaner', 'Journalist', 'Artist', 'Doctor',
        'Teacher', 'Entrepreneur', 'Farmer', 'Writer', 'Mechanic',
        'Manager', 'Engineer', 'Musician', 'Lawyer', 'Scientist',
        'Unemployed', 'Student', 'Media_Manager', 'Accountant',
        'Developer', 'Pension'],help="Represents the occupation of the person") # All occupations in the dataset is included
    annual_income = st.number_input("Annual Income (USD)", min_value=0.0, step=0.01,help="Represents the annual income of the person")
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0 , step=0.1,help="Represents the interest rate on credit card") #The maximum value in the dataset is 34

with col2:
    num_bank_accounts = st.slider("Number of Bank Accounts", 0, 25,help="Represents the number of bank accounts a person holds") #The maximum value in the dataset is 11
    num_credit_cards = st.slider("Number of Credit Cards", 0, 25,help="Represents the number of other credit cards held by a person") #The maximum value in the dataset is 11
    num_of_loans = st.slider("Number of Loans", 1, 10,help="Represents the number of loans taken from the bank") # The maximum value in the dataset is 9
    type_of_loan = st.multiselect("Type of Loan", ['Credit-Builder Loan', 'Home Equity Loan', 'Not Specified', 'Payday Loan', 'Auto Loan', 'Personal Loan', 'Mortgage Loan', 'Student Loan', 'Debt Consolidation Loan'],default='Not Specified',help="Represents the type of loan taken by the person")

    if len(type_of_loan) != num_of_loans:
        st.error("The number of loans must match the number of selected types of loans.")
    else:
        type_of_loan_str = tuple(type_of_loan)

with col3:
    delay_from_due_date = st.number_input("Delay from Due Date (days)", min_value=0,help="Represents the number of days the payment is delayed from the payment date")
    num_of_delayed_payments = st.number_input("Number of Delayed Payments", min_value=0,help="Represents the average number of delayed payments made by the person")
    changed_credit_limit = st.number_input("Changed Credit Limit %", min_value=0.0, step=0.01, help="Represents the percentage change in credit card limit")
    num_of_credit_inquiries = st.number_input("Number of Credit Inquiries", min_value=0,help="Represents the number of credit card inquiries")
    credit_mix = st.selectbox("Credit Mix", ['Bad', 'Standard', 'Good'] ,help="Represents the classification of the mix of credits") # All credit mix in the dataset is included
    outstanding_debt = st.number_input("Outstanding Debt (USD)", min_value=0.0, step=0.01,help="Represents the remaining debt to be paid (in USD)")

payment_of_min_amount = st.selectbox("Payment of Minimum Amount", ["Yes", "No"],help="Represents whether only the minimum amount was paid by the person")


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Month": month,
        "Occupation": occupation,
        "Annual_Income": annual_income,
        "Num_Bank_Accounts": num_bank_accounts,
        "Num_Credit_Card": num_credit_cards,
        "Interest_Rate": interest_rate,
        "Num_of_Loan": num_of_loans,
        "Type_of_Loan": type_of_loan_str,
        "Delay_from_due_date": delay_from_due_date,
        "Num_of_Delayed_Payment": num_of_delayed_payments,
        "Changed_Credit_Limit": changed_credit_limit,
        "Num_Credit_Inquiries": num_of_credit_inquiries,
        "Credit_Mix": credit_mix,
        "Outstanding_Debt": outstanding_debt,
        "Payment_of_Min_Amount": payment_of_min_amount
    }])

    prediction = model_c.predict(input_data)
    score = prediction[0]

    st.success(f"Your credit score is: {score}")
    st.balloons()
