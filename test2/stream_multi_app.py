import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.DataFrame(px.data.gapminder())

st.header("National Statistics")

clist = df['country'].unique()

country = st.sidebar.selectbox("Select a countr:", clist)

fig = px.line(df[df['country'] == country],
x = "year", y = "gdpPercap", title=country)

st.plotly_chart(fig)