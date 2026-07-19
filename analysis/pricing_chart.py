import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv = os.path.join(BASE_DIR,"data","processed","competitor_master.csv")

df = pd.read_csv(csv)

prices = {
    "ChatGPT":20,
    "Claude":20,
    "Gemini":20,
    "Cursor":20,
    "Perplexity":20,
    "GitHub Copilot":10,
    "Canva AI":15,
    "Adobe Firefly":10,
    "Notion AI":10,
    "Jasper":49
}

df["Price"] = df["Company"].map(prices)

plt.figure(figsize=(10,6))

plt.barh(df["Company"],df["Price"])

plt.xlabel("Monthly Price ($)")

plt.title("AI Tools Entry Paid Plan Comparison")

plt.tight_layout()

path=os.path.join(BASE_DIR,"outputs","pricing_comparison.png")

plt.savefig(path)

print("Pricing chart saved.")