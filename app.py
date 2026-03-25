import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("🧾 Invoice Anomaly Detection App")

# Sample dataset
data = pd.DataFrame({
    'Amount': [1000, 1500, 2000, 2500, 3000, 10000, 1200, 1800, 2200, 50000],
    'Quantity': [2, 3, 1, 4, 2, 10, 2, 3, 2, 20]
})

st.subheader("📁 Invoice Data")
st.dataframe(data)

# Model
model = IsolationForest(contamination=0.2)
model.fit(data)

data['Anomaly'] = model.predict(data)

# Convert (-1 = anomaly, 1 = normal)
data['Anomaly'] = data['Anomaly'].map({1: "Normal", -1: "Anomaly"})

st.subheader("🔍 Detection Result")
st.dataframe(data)

# Input section
st.subheader("➕ Check New Invoice")

amount = st.number_input("Amount", value=2000)
quantity = st.number_input("Quantity", value=2)

if st.button("Check"):
    result = model.predict([[amount, quantity]])
    if result[0] == -1:
        st.error("🚨 Anomaly Detected!")
    else:
        st.success("✅ Normal Invoice")

# Graph
st.subheader("📊 Visualization")

fig, ax = plt.subplots()
ax.scatter(data['Amount'], data['Quantity'])
ax.set_xlabel("Amount")
ax.set_ylabel("Quantity")

st.pyplot(fig)