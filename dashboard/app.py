import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px

st.set_page_config(
    page_title="AI Competitive Intelligence Dashboard",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "competitive_intelligence.db")

conn = sqlite3.connect(db_path)

df = pd.read_sql("SELECT * FROM competitors", conn)

conn.close()

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

st.title("🤖 AI Tools Competitive Intelligence Dashboard")

col1,col2,col3=st.columns(3)

col1.metric("Competitors",len(df))
col2.metric("Categories",df["Category"].nunique())
col3.metric("Free Plans",(df["Free_Plan"]=="Yes").sum())

st.divider()

st.subheader("Competitor Dataset")

st.dataframe(df,use_container_width=True)

st.divider()

fig=px.bar(
    df,
    x="Company",
    y="Price",
    color="Category",
    title="Entry Paid Plan Comparison"
)

st.plotly_chart(fig,use_container_width=True)

fig2=px.pie(
    df,
    names="Category",
    title="Market Share by Category"
)

st.plotly_chart(fig2,use_container_width=True)

st.divider()

st.subheader("Companies with Free Plans")

st.dataframe(df[df["Free_Plan"]=="Yes"])

st.divider()

st.success("Competitive Intelligence Dashboard Developed for Aarivya Labs Internship")