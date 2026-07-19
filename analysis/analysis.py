import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, "database", "competitive_intelligence.db")

conn = sqlite3.connect(db_path)

df = pd.read_sql("SELECT * FROM competitors", conn)

conn.close()

print(df)

print("\n========== SUMMARY ==========")

print("\nTotal Competitors:", len(df))

print("\nCategories:")

print(df["Category"].value_counts())

print("\nCompanies Offering Free Plan:")

print(df[df["Free_Plan"]=="Yes"][["Company","Entry_Paid_Plan"]])

category_counts = df["Category"].value_counts()

plt.figure(figsize=(8,5))

category_counts.plot(kind="bar")

plt.title("AI Tool Categories")

plt.xlabel("Category")

plt.ylabel("Number of Competitors")

plt.tight_layout()

output_path = os.path.join(BASE_DIR,"outputs","category_distribution.png")

plt.savefig(output_path)

print("\nChart Saved Successfully!")