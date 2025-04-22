import streamlit as st
from weight import weighing  

# 🧭 Sidebar Navigation
st.set_page_config(page_title="AirSpy - AQI through MLP", layout="centered")
st.sidebar.title("🌐 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Technique", "Prediction"])

# 🏠 Home Page
if page == "Home":
    st.title("🌍 AirSpy ")
    st.markdown("""
    **AirSpy** is a state-of-the-art air quality classifier that uses **Multi-Layered Perceptrons (MLPs)** and **Geospatial Data** to determine air quality.  
    Our model analyzes air quality based on six major pollutants:
    
    - **NO₂ (Nitrogen Dioxide)**
    - **O₃ (Ozone)**
    - **PM2.5**
    - **PM10**
    - **SO₂ (Sulfur Dioxide)**
    - **CO (Carbon Monoxide)**

    🧑‍💻 **How it works:**  
    AirSpy utilizes data from **Google Earth Engine (GEE)**, APIs, and multiple MLPs trained on region-specific pollutant data to generate AQI classifications.  
    
    👉 Use the sidebar to explore the app and learn more about the techniques and predictions.
    """)

# ℹ️ About Page
elif page == "About":
    st.title("ℹ️ About AirSpy")
    st.markdown("""
    **AirSpy** is a powerful tool designed to analyze air quality in real-time based on **six critical pollutants**: NO₂, O₃, PM2.5, PM10, SO₂, and CO.  
    The project combines **Deep Learning (MLPs)** with **Geospatial Data** to predict AQI.

    ### Project Workflow:
    - Initially, **1000 images** of NO₂ and O₃ band data were extracted from **Google Earth Engine (GEE)**.
    - The images were processed, and their data was **normalized** and converted to standard units.
    - A **Multi-Layered Perceptron (MLP)** was then trained on these images.
    - For the next pollutants, **PM2.5** and **PM10** data were fetched using APIs and used to train separate MLPs.
    - For **SO₂** and **CO**, **text-based data** was taken from **Google Earth Engine**, and separate MLPs were trained.

    ### How It Works:
    Each pollutant has its own dedicated MLP, and a **weighted approach** is used to combine their individual AQI classifications to determine the final overall air quality score.

    **Technologies Used:**
    - **Python**
    - **TensorFlow / Keras** for MLP models
    - **Google Earth Engine (GEE)** for image data
    - **APIs** for PM2.5 and PM10 data extraction
    - **Streamlit** for the web app interface

    The AQI classification is then derived using a weighted average approach that considers the contribution of each pollutant.
    """)

# ⚙️ Technique Page
# ⚙️ Technique Page
elif page == "Technique":
    st.title("🧪 Technique Used in AirSpy")
    st.markdown("""
    **AirSpy** uses a multi-stage approach to classify air quality based on pollutant levels. Here's how the technique works:

    ### 1. **Data Collection:**
    - **NO₂ and O₃** data: Images were extracted from **Google Earth Engine (GEE)**, focusing on 15 different regions with 1000 images. These images were analyzed, and pollutant data was extracted and converted to standard units.
    
    ### 2. **Training the First MLP:**
    - A **Multi-Layered Perceptron (MLP)** was trained on the NO₂ and O₃ data to predict the air quality for these two pollutants.

    ### 3. **Training Additional MLPs:**
    - **PM2.5** and **PM10** data were fetched via **API**, and separate MLPs were trained for each of these pollutants.
    - **SO₂** and **CO** data were gathered through **text data** from **Google Earth Engine**, and another MLP was trained for these pollutants.

    ### 4. **Weighted Approach:**
    Once each pollutant’s AQI was predicted using the respective MLP, a **weighted formula** was used to combine the AQI scores from all pollutants to derive the final **overall AQI score**.

    ### 5. **AQI Categorization:**
    The AQI score is categorized as follows:
    - **Good**: AQI 0–50
    - **Moderate**: AQI 51–100
    - **Unhealthy for Sensitive Groups**: AQI 101–150
    - **Unhealthy**: AQI 151–200
    - **Very Unhealthy**: AQI 201–300
    - **Hazardous**: AQI > 300

    This approach ensures that the final AQI score reflects a holistic view of the air quality, considering multiple pollutants' effects.
    
    ### What is a Multi-Layered Perceptron (MLP)?
    **Multi-Layered Perceptron (MLP)** is a type of **artificial neural network** (ANN) that consists of multiple layers of neurons (also called nodes). These layers are structured as follows:
    - **Input Layer**: Takes the input data (pollutant concentrations in this case).
    - **Hidden Layers**: A series of layers where computations are performed. Each neuron in these layers takes inputs, processes them, and passes them to the next layer.
    - **Output Layer**: Produces the final result — in this case, the AQI classification.

    MLPs are called **feedforward neural networks** because data flows in one direction: from the input layer, through the hidden layers, and finally to the output layer. The hidden layers are responsible for learning complex patterns in the data by adjusting weights and biases, making them ideal for predicting values like AQI scores based on complex environmental data.

    ### How Does MLP Work in AirSpy?
    In **AirSpy**, MLPs were specifically trained for each pollutant to predict its contribution to the overall air quality:
    - **NO₂ and O₃ data** were fed into the first MLP to predict their respective AQI scores.
    - **PM2.5 and PM10 data** were fed into separate MLPs to classify their contribution to air quality.
    - **SO₂ and CO text data** were processed through an MLP to predict their effects on AQI.

    The strength of MLP lies in its ability to learn non-linear relationships between input variables, making it suitable for complex environmental data where pollutant levels don’t follow simple linear patterns.

    ### Weights Used:
    - **NO₂**: 20%
    - **O₃**: 10%
    - **PM2.5**: 30%
    - **PM10**: 25%
    - **SO₂**: 10%
    - **CO**: 5%

    The final AQI is then categorized according to the standard guidelines.
    """)


# 📈 Prediction Page
elif page == "Prediction":
    st.title("📈 Predict Air Quality")
    st.subheader("Enter pollutant concentrations (in µg/m³):")

    no2 = st.number_input("NO₂ (Nitrogen Dioxide)", min_value=0.0, value=0.0)
    o3 = st.number_input("O₃ (Ozone)", min_value=0.0, value=0.0)
    pm25 = st.number_input("PM2.5", min_value=0.0, value=0.0)
    pm10 = st.number_input("PM10", min_value=0.0, value=0.0)
    so2 = st.number_input("SO₂ (Sulfur Dioxide)", min_value=0.0, value=0.0)
    co = st.number_input("CO (Carbon Monoxide)", min_value=0.0, value=0.0)

    if st.button("Check Air Quality"):
        final_aqi, category = weighing(no2, o3, pm25, pm10, so2, co)
        st.success(f"✅ Final AQI Score: {final_aqi:.2f}")
        st.markdown(f"### ☁️ Air Quality Classification: **{category}**")
