# main.py
from extract_weather import extract_weather_data
from load_to_postgres import load_to_postgres
from config import DB_URL, TABLE_NAME

def run_pipeline():
    df = extract_weather_data()
    if df is None:
        print("🚫 No data to load due to API failure.")
        return

    print("✅ Weather data extracted:")
    print(df)

    load_to_postgres(df, DB_URL, TABLE_NAME)
    print("✅ Data loaded into PostgreSQL.")

if __name__ == "__main__":
    run_pipeline()
