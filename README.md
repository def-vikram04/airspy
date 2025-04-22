🌍 AirSpy — Intelligent Air Quality Analyzer
AirSpy is an intelligent air quality analysis system that leverages Multi-Layered Perceptron (MLP) models and Geospatial Data to classify and predict the Air Quality Index (AQI) based on six major pollutants.

📌 Features
🌐 Geospatial Intelligence using Google Earth Engine

🧠 Neural Network-based classification using multiple MLPs

🔬 Support for six key pollutants:

NO₂ (Nitrogen Dioxide)

O₃ (Ozone)

PM2.5

PM10

SO₂ (Sulfur Dioxide)

CO (Carbon Monoxide)

🧮 Weighted AQI Score combining outputs from all MLP models

⚡ Fast & interactive Streamlit Web App

🧪 How It Works

Step	Process
1️⃣	Data for NO₂ and O₃ collected from Google Earth Engine using satellite band images from 15 regions (1000 images)
2️⃣	Images processed and converted to standard units, then used to train the 1st MLP
3️⃣	Real-time PM2.5 and PM10 data fetched via public APIs, and fed into 2nd and 3rd MLPs
4️⃣	SO₂ and CO values extracted as text data from Google Earth Engine, then processed via the 4th MLP
5️⃣	Each MLP outputs its individual AQI classification
6️⃣	Final AQI is calculated using a weighted formula for pollutant importance
7️⃣	AQI is mapped to categories: Good, Moderate, Unhealthy, etc.
🧠 Tech Stack
Frontend: Streamlit

Backend: Python, NumPy, scikit-learn / TensorFlow

ML Models: Multi-Layered Perceptrons (Neural Networks)

Data Sources:

Google Earth Engine

Open AQ & similar APIs

🏁 Getting Started
🔧 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/airspy.git
cd airspy
pip install -r requirements.txt
▶️ Run the App Locally
bash
Copy
Edit
streamlit run app.py
📊 AQI Classification

AQI Range	Category
0–50	✅ Good
51–100	🟡 Moderate
101–150	🟠 Unhealthy for Sensitive Groups
151–200	🔴 Unhealthy
201–300	🟣 Very Unhealthy
301+	⚫ Hazardous
📦 Deployment
Deploy to Streamlit Cloud easily:

Push your code to GitHub

Log in to Streamlit Cloud

Connect your GitHub repo

Deploy and go live!

🤖 Why Use AirSpy Over a Weather App?

Feature	Weather App	AirSpy
Uses Satellite Band Data	❌	✅
Machine Learning Based Predictions	❌	✅
Region-wise AQI Modeling	❌	✅
Pollutant-wise Classification	Limited	✅
Weighted Intelligence	❌	✅
👨‍💻 Authors
Arka Ghosh (EE2018/020)

Sayan Dalui (EE2018/022)

Bhaswati Chakraborty (EE2018/052)

Srija Basu (EE2018/057)

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

