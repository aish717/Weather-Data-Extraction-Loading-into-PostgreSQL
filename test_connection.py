from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:postgre@localhost:5432/weatherdb")
with engine.connect() as conn:
    print("✅ Connection successful!")
