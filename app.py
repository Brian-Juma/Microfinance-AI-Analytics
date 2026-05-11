import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample_portfolio.csv")

st.title("Microfinance AI Analytics")

st.dataframe(df)

st.bar_chart(df.groupby("branch")["actual_payment"].sum())

streamlit run app.py
