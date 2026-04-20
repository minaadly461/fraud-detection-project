import streamlit as st
import pandas as pd 
import joblib
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'model', 'fraud_detection_pipeline.pkl')

try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: Could not find the model at {model_path}")


st.title("Fraud Detection APP")

st.markdown("enter the transaction details and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg = st.number_input("old Balance (Sender)",min_value=0.0,value=10000.0)
newbalanceOrg = st.number_input("New Balance (Sender)",min_value=0.0,value=9000.0)
oldbalanceDest = st.number_input("Old Balance (receiver)",min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Balance (receiver)",min_value=0.0,value=0.0)


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrg":newbalanceOrg,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }])

    prediction = model.predict(input_data)[0]


    st.subheader(f"prediction :'{int(prediction)}'")


    if prediction ==1 :
        st.error("this transaction can be fraud")

    else : 
        st.success("This transaction is not fraud")




