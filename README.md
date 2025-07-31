# 🕵️‍♀️ Fraud Detection Streamlit App

This Streamlit app uses a fine-tuned XGBoost machine learning model to predict fraudulent financial transactions based on transaction features.

## 💡 Features
- Upload CSV file for predictions
- Real-time fraud detection output
- Download prediction results

## 🔧 Technologies
- Python
- XGBoost
- Scikit-learn
- Pandas, NumPy
- Streamlit

## 🚀 How to Run
1. Clone the repository
2. Install requirements:
   pip install -r requirements.txt

4.  Run the app:

## 📝 Sample Input Format
Ensure your CSV contains the following columns:
['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig',
'oldbalanceDest', 'newbalanceDest']


## 📁 File Structure
- `app.py`: Streamlit app code
- `xgb_model.pkl`: Trained model file
- `sample_transactions.csv`: Example input file
- `requirements.txt`: Dependencies list


