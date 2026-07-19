import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

def save_csv(df, filename):
    os.makedirs(RAW_DIR, exist_ok=True)
    df.to_csv(os.path.join(RAW_DIR, filename), index=False)
    print("Saved:", filename)