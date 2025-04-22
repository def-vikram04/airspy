# In weighted.ipynb
import numpy as np

weights = np.array([0.20, 0.10, 0.30, 0.25, 0.10, 0.05])

def weighing(no2, o3, pm25, pm10, so2, co):
    normalized = np.array([
        (no2 / 400) * 500,
        (o3 / 200) * 500,
        (pm25 / 250) * 500,
        (pm10 / 500) * 500,
        (so2 / 800) * 500,
        (co / 4000) * 500
    ])
    final_aqi = np.dot(weights, normalized)

    if final_aqi <= 50:
        category = "Good"
    elif final_aqi <= 100:
        category = "Satisfactory"
    elif final_aqi <= 200:
        category = "Moderate"
    elif final_aqi <= 300:
        category = "Poor"
    elif final_aqi <= 400:
        category = "Very Poor"
    else:
        category = "Severe (Hazardous)"
    
    return final_aqi, category
