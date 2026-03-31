import streamlit as st
import pandas as pd

st.title("🧾 Invoice Anomaly Detection (Simple)")

# Sample data
data = pd.DataFrame({
    "Amount": [1000, 1500, 2000, 2500, 3000, 50000],
})

st.subheader("Dataset")
st.write(data)

# Simple anomaly logic (no sklearn)
threshold = 10000

data["Anomaly"] = data["Amount"].apply(
    lambda x: "Anomaly" if x > threshold else "Normal"
)

st.subheader("Result")
st.write(data)

# ✅ Visualization (added)
st.subheader("📊 Visualization")

# Graph 1: Amount distribution
st.write("Amount Distribution")
st.bar_chart(data["Amount"])

# Graph 2: Normal vs Anomaly count (best 🔥)
st.write("Anomaly vs Normal Count")
st.bar_chart(data["Anomaly"].value_counts())

# User input
st.subheader("Check New Invoice")

amount = st.number_input("Enter Amount", value=2000)

if st.button("Check"):
    if amount > threshold:
        st.error("🚨 Anomaly Detected!")
    else:
        st.success("✅ Normal Invoice")
