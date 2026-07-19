import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, "database", "competitive_intelligence.db")

conn = sqlite3.connect(db_path)

query = "SELECT * FROM competitors"

df = pd.read_sql(query, conn)

print(df)

conn.close()