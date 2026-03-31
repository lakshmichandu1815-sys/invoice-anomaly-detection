import streamlit as st
import pandas as pd

st.set_page_config(page_title="Invoice Detection", layout="centered")

st.title("🧾 Automated Invoice Anomaly Detection")
st.markdown("Upload invoice data and detect anomalies easily")

# File upload
file = st.file_uploader("📂 Upload Invoice CSV", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    st.subheader("📊 Uploaded Data")
    st.dataframe(data)

    # Check column
    if "Amount" in data.columns:

        threshold = st.slider("⚙️ Set Threshold", 1000, 100000, 10000)

        data["Status"] = data["Amount"].apply(
            lambda x: "🚨 Anomaly" if x > threshold else "✅ Normal"
        )

        st.subheader("📈 Results")
        st.dataframe(data)

        # Metrics
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Records", len(data))

        with col2:
            anomalies = data[data["Status"] == "🚨 Anomaly"].shape[0]
            st.metric("Anomalies", anomalies)

        
        # 📊 Visualization
st.subheader("📊 Visualization")

# Graph 1: Amount distribution (clean)
st.write("Amount Distribution")
st.bar_chart(data["Amount"])

# Graph 2: Normal vs Anomaly (important)
st.write("Anomaly vs Normal Count")
st.bar_chart(data["Status"].value_counts())
        

    else:
        st.error("❌ CSV must contain 'Amount' column")

else:
    st.info("👆 Upload a CSV file to start")
