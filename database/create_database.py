import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, "database", "competitive_intelligence.db")

csv_path = os.path.join(BASE_DIR, "data", "processed", "competitor_master.csv")

conn = sqlite3.connect(db_path)

df = pd.read_csv(csv_path)

df.to_sql(
    "competitors",
    conn,
    if_exists="replace",
    index=False
)

print(df)

print("\nDatabase Created Successfully!")

conn.close()