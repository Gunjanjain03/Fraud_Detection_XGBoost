import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('xgb_model.pkl')

st.title("💸 Fraud Detection App")

uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data Preview")
    st.write(data.head())

    # Make predictions
    if st.button("Predict Fraud"):
                # Replace this line:
        # predictions = model.predict(data)

        # Add this preprocessing before prediction:
        data['type_CASH_OUT'] = (data['type'] == 'CASH_OUT').astype(int)
        data['type_TRANSFER'] = (data['type'] == 'TRANSFER').astype(int)

        # Drop original 'type' column
        data = data.drop(columns=['type'])

        # Ensure column order matches training
        expected_cols = model.feature_names_in_
        # Create engineered features if not present
    if 'errorBalanceorig' not in data.columns:
        data['errorBalanceorig'] = data['oldbalanceOrg'] - data['newbalanceOrig'] - data['amount']

    if 'errorBalanceDest' not in data.columns:
        data['errorBalanceDest'] = data['newbalanceDest'] - data['oldbalanceDest'] - data['amount']

        data = data[expected_cols]

        # Now predict
        predictions = model.predict(data)

        
        data['Fraud_Prediction'] = predictions
        st.subheader("Prediction Results")
        st.write(data[['Fraud_Prediction']])
        st.download_button("Download Predictions", data.to_csv(index=False), "predictions.csv", "text/csv")
