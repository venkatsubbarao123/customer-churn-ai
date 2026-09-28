from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from train_model import DATA_PATH, MODEL_PATH, create_demo_data, train

st.set_page_config(page_title="Customer Churn AI", page_icon="📊", layout="wide")

st.title("Customer Churn AI")
st.caption("Estimate customer churn risk from a few account signals.")

if not MODEL_PATH.exists():
    with st.spinner("Preparing the demo model..."):
        train()

model = joblib.load(MODEL_PATH)

with st.sidebar:
    st.header("Customer profile")
    tenure_months = st.slider("Tenure (months)", 1, 72, 12)
    monthly_charges = st.number_input("Monthly charges", min_value=20.0, max_value=150.0, value=75.0, step=1.0)
    support_calls = st.slider("Support calls", 0, 10, 2)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    has_internet = st.selectbox("Has internet service", ["Yes", "No"])
    predict = st.button("Predict churn", type="primary", use_container_width=True)

customer = pd.DataFrame(
    [
        {
            "tenure_months": tenure_months,
            "monthly_charges": monthly_charges,
            "support_calls": support_calls,
            "contract": contract,
            "has_internet": has_internet,
        }
    ]
)

if predict:
    churn_probability = float(model.predict_proba(customer)[0, 1])
    prediction = churn_probability >= 0.5
    metric_col, detail_col = st.columns([1, 2])
    with metric_col:
        st.metric("Churn probability", f"{churn_probability:.1%}")
    with detail_col:
        if prediction:
            st.error("High churn risk. Consider a retention offer or proactive outreach.")
        else:
            st.success("Lower churn risk based on this profile.")

st.subheader("Customer details")
st.dataframe(customer, use_container_width=True, hide_index=True)

with st.expander("About this starter model"):
    st.write("The first run creates synthetic customer data and trains a logistic regression model. Replace data/customer_churn.csv with your own dataset when you are ready.")
