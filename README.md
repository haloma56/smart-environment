# 🌱 Smart Environment Monitoring System

## 📌 Project Description

Smart Environment Monitoring System is a Python-based application designed to monitor and analyze environmental data such as temperature, humidity, and air quality.

The system analyzes the collected data, calculates average values, determines the environmental status, and provides a visual dashboard using Streamlit.

## 🎯 Objectives

The main objectives of this project are:

- Monitor environmental conditions.
- Analyze temperature, humidity, and air quality data.
- Detect normal, warning, and critical environmental conditions.
- Display environmental data through an interactive dashboard.
- Containerize the application using Docker.
- Manage and publish the project using Git and GitHub.

## 🛠️ Technologies Used

- **Python**
- **Pandas** – data processing
- **Matplotlib** – data visualization
- **Streamlit** – interactive dashboard
- **Docker** – application containerization
- **Git / GitHub** – version control and project management

## 📁 Project Structure

```text
smart-environment/
│
├── app/
│   ├── main.py
│   └── dashboard.py
│
├── data/
│   └── environment_data.csv
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Environmental Data

The application works with environmental measurements including:

- Temperature (°C)
- Humidity (%)
- Air Quality

The data is stored in:

```text
data/environment_data.csv
```

## 🚀 Run the Application with Python

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

Then start the Streamlit dashboard:

```bash
python -m streamlit run app/dashboard.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

## 🐳 Run the Application with Docker

Build the Docker image:

```bash
docker build -t smart-environment .
```

Run the container:

```bash
docker run -p 8501:8501 smart-environment
```

Then open:

```text
http://localhost:8501
```

## 📈 Dashboard

The Streamlit dashboard provides:

- Average temperature
- Average humidity
- Average air quality
- Environmental status
- Environmental data table
- Data visualization

## 🔎 Environmental Status

The application classifies environmental conditions according to predefined thresholds.

Possible statuses include:

- **NORMAL**
- **WARNING**
- **CRITICAL**

## 🔧 Project Workflow

```text
Environmental Data
        ↓
      Python
        ↓
   Data Analysis
        ↓
    Streamlit
        ↓
   Visualization
        ↓
     Docker
        ↓
   Git / GitHub
```

## 👩‍💻 Author

**Ahlem**

## 📄 License

This project was developed for educational purposes.
