import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search of Happiness")
option = st.selectbox("Select the data for X-axis",("gdp","happiness","generosity"))
options = st.selectbox("Select the data for Y-axis",("gdp","happiness","generosity"))

x = None
match option:
    case "gdp":
        x = df["gdp"]
    case "happiness":
        x = df["happiness"]
    case "generosity":
        x = df["generosity"]

y = None
match options:
    case "gdp":
        y = df["gdp"]
    case "happiness":
        y= df["happiness"]
    case "generosity":
        y = df["generosity"]

st.subheader(f"{option} and {options}")

figure = px.scatter(x=x, y=y, labels={"x": option, "y": options})
st.plotly_chart(figure)
