import pandas as pd
import streamlit as st  # type: ignore[import-not-found]
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Smart Environment",
    page_icon="🌱",
    layout="wide"
)

# Title
st.title("🌱 Smart Environment Monitoring System")
st.write("Environmental data monitoring and analysis dashboard")

# Load data
data = pd.read_csv("data/environment_data.csv")

# Calculate statistics
average_temperature = data["temperature"].mean()
average_humidity = data["humidity"].mean()
average_air_quality = data["air_quality"].mean()

# Display indicators
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌡 Average Temperature",
        f"{average_temperature:.2f} °C"
    )

with col2:
    st.metric(
        "💧 Average Humidity",
        f"{average_humidity:.2f} %"
    )

with col3:
    st.metric(
        "🌫 Average Air Quality",
        f"{average_air_quality:.2f}"
    )

# Environmental status
st.subheader("Environmental Status")

if average_temperature > 35 or average_air_quality > 100:
    st.error("⚠️ CRITICAL: Poor environmental conditions")
elif average_temperature > 30 or average_air_quality > 70:
    st.warning("⚠️ WARNING: Environmental conditions need attention")
else:
    st.success("✅ NORMAL: Environmental conditions are good")

# Data table
st.subheader("Environmental Measurements")
st.dataframe(data)

# Chart
st.subheader("📊 Environmental Measurements")

fig, ax = plt.subplots()

ax.plot(
    data["temperature"],
    label="Temperature"
)

ax.plot(
    data["humidity"],
    label="Humidity"
)

ax.plot(
    data["air_quality"],
    label="Air Quality"
)

ax.set_xlabel("Measurement")
ax.set_ylabel("Value")
ax.legend()
ax.grid()

st.pyplot(fig)