import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Customer Segmentation AI",
    page_icon="👥",
    layout="wide"
)

# --- MODEL LOADING ---
# Using cache_resource ensures the model stays in memory and doesn't reload on every click
@st.cache_resource
def load_artifacts():
    try:
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        with open('kmeans_model.pkl', 'rb') as f:
            kmeans = pickle.load(f)
        return scaler, kmeans
    except FileNotFoundError:
        return None, None

scaler, kmeans = load_artifacts()

# --- CONSTANTS & MAPPINGS ---
EDUCATION_MAP = {'Undergraduate': 0, 'Graduate': 1, 'Postgraduate': 2}
MARITAL_MAP = {'Partnered': 0, 'Single': 1}
RESPONSE_MAP = {'No': 0, 'Yes': 1}

CLUSTER_INFO = {
    0: {"name": "Average Mainstream", "color": "blue", "desc": "Steady customers with moderate spending habits."},
    1: {"name": "Budget-Conscious", "color": "green", "desc": "Price-sensitive; highly responsive to discounts and deals."},
    2: {"name": "High-Value", "color": "orange", "desc": "High income earners who shop frequently across all channels."},
    3: {"name": "Premium Loyal", "color": "red", "desc": "Our top tier; high spending and very high campaign engagement."}
}

# --- UI HEADER ---
st.title("👥 Customer Personality Analysis")
st.markdown("""
    Use this tool to classify customers into behavioral segments based on demographic and purchasing data.
    *Simply fill in the details below and click **Predict Segment**.*
""")

if scaler is None or kmeans is None:
    st.error("⚠️ Error: Model files (`scaler.pkl` or `kmeans_model.pkl`) not found in the directory.")
    st.stop()

# --- INPUT FORM ---
with st.form("customer_form"):
    st.subheader("Customer Profile & Behavior")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🧬 Demographics")
        age = st.number_input("Age", 18, 100, 45)
        income = st.number_input("Annual Income ($)", 0, 200000, 50000, step=500)
        education = st.selectbox("Education Level", options=list(EDUCATION_MAP.keys()))
        marital = st.selectbox("Marital Status", options=list(MARITAL_MAP.keys()))

    with col2:
        st.info("🛒 Purchase History")
        total_spend = st.number_input("Total Spending ($)", 0, 10000, 500)
        total_purchases = st.number_input("Total Purchases (Count)", 0, 100, 15)
        recency = st.number_input("Recency (Days since last buy)", 0, 365, 30)
        dependents = st.number_input("Total Dependents", 0, 5, 1)

    with col3:
        st.info("📱 Engagement")
        web_visits = st.number_input("Web Visits / Month", 0, 50, 5)
        deals = st.number_input("Deals Purchased", 0, 20, 2)
        campaigns = st.slider("Campaigns Accepted", 0, 5, 0)
        response = st.radio("Last Campaign Response", ["No", "Yes"], horizontal=True)

    # Center the button
    _, mid_col, _ = st.columns([1, 1, 1])
    submit = mid_col.form_submit_button("🚀 Predict Segment", use_container_width=True)

# --- PREDICTION LOGIC ---
if submit:
    # 1. Prepare Feature Array (Ensuring exact order as training)
    # Order: Education, Marital_Status, Income, Recency, NumDealsPurchases,
    # NumWebVisitsMonth, Response, Age, Total_Spend, Total_Purchases, Total_Dependents, Total_Campaigns_Accepted

    raw_data = pd.DataFrame([{
        'Education': EDUCATION_MAP[education],
        'Marital_Status': MARITAL_MAP[marital],
        'Income': income,
        'Recency': recency,
        'NumDealsPurchases': deals,
        'NumWebVisitsMonth': web_visits,
        'Response': RESPONSE_MAP[response],
        'Age': age,
        'Total_Spend': total_spend,
        'Total_Purchases': total_purchases,
        'Total_Dependents': dependents,
        'Total_Campaigns_Accepted': campaigns
    }])

    # 2. Transform & Predict
    try:
        scaled_data = scaler.transform(raw_data)
        cluster_id = kmeans.predict(scaled_data)[0]
        result = CLUSTER_INFO.get(cluster_id, {"name": "Unknown", "color": "gray", "desc": "N/A"})

        # 3. Display Results
        st.divider()
        st.balloons()

        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric(label="Predicted Cluster", value=f"Cluster {cluster_id}")
        with c2:
            st.success(f"### Segment: **{result['name']}**")
            st.write(f"**Insight:** {result['desc']}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# --- FOOTER ---
with st.expander("ℹ️ About the Clusters"):
    for cid, info in CLUSTER_INFO.items():
        st.write(f"**{info['name']}**: {info['desc']}")
