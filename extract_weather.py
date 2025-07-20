# extract_weather.py

import requests
import pandas as pd
from datetime import datetime
from config import API_KEY

def extract_weather_data():
    CITY = "Bengaluru"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    url = f"{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    print("✅ API Response:")
    print(data)

    # Handle failed API response
    if response.status_code != 200 or "main" not in data:
        print("❌ Failed to get weather data. Status:", data.get("message", "Unknown error"))
        return None

    df = pd.DataFrame([{
        "city": CITY,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "timestamp": datetime.now()
    }])

    return df
