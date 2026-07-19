import pandas as pd
import sqlite3
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db=os.path.join(BASE_DIR,"database","competitive_intelligence.db")

conn=sqlite3.connect(db)

df=pd.read_sql("SELECT * FROM competitors",conn)

conn.close()

print("="*60)
print("AI TOOLS STRATEGIC RECOMMENDATIONS")
print("="*60)

coding=df[df["Category"]=="Coding AI"]

general=df[df["Category"]=="General AI"]

print("\nGeneral AI Leaders")

print(general["Company"].tolist())

print("\nCoding AI Leaders")

print(coding["Company"].tolist())

print("\nRecommendations")

print("- Offer Freemium Plans")
print("- Maintain $10-$20 Entry Pricing")
print("- Bundle with Existing Ecosystem")
print("- Introduce Enterprise Plans")
print("- Differentiate Through Features")

print("\nAnalysis Completed Successfully")