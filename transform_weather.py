# transform_weather.py
from datetime import datetime

def transform_weather_data(df):
    df["timestamp"] = datetime.now()
    return df