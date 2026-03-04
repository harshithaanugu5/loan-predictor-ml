import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Citi Risk Assessment Tool")
st.title("🏦 Professional Loan Risk Engine")

# 1. Improved Model Training
@st.cache_data
def train_model():
    df = pd.read_csv('loan_data.csv')
    
    # Convert text to numbers (Encoding)
    df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
    df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})
    
    X = df[['ApplicantIncome', 'LoanAmount', 'Credit_History', 'Education']]
    y = df['Loan_Status']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_model()

# 2. UI Layout
st.sidebar.header("Applicant Profile")
income = st.sidebar.number_input("Monthly Income ($)", value=5000)
loan = st.sidebar.number_input("Requested Loan ($)", value=200)
credit = st.sidebar.selectbox("Credit History", options=[1, 0], format_func=lambda x: "Clean" if x == 1 else "Issues")
edu = st.sidebar.selectbox("Education", options=["Graduate", "Not Graduate"])

# 3. Real-World Prediction Logic
if st.button("Run Risk Analysis"):
    # Prepare input
    edu_val = 1 if edu == "Graduate" else 0
    prediction = model.predict([[income, loan, credit, edu_val]])
    
    # Calculate DTI for the UI
    dti = (loan / income) if income > 0 else 0
    
    st.subheader("Analysis Results")
    if prediction[0] == 1:
        st.success("✅ LOAN APPROVED: Low Risk Profile")
    else:
        st.error("❌ LOAN REJECTED: High Risk Profile")

    # Add professional insight
    st.info(f"**Debt-to-Income Analysis:** Your requested loan is {dti:.2f}x your monthly income.")
    if dti > 10:
        st.warning("⚠️ High Debt-to-Income detected. This is the primary reason for rejection.")
