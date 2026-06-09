import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Streamlit Charts")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader('Bar Chart')
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter chart")
Scadata = pd.DataFrame({
    'x' : np.random.randn(100),
    'y' : np.random.randn(100)
})
st.scatter_chart(Scadata)

st.subheader("MAP")
MapData = pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[37.6,-122.4],
    columns=['lat','lon']
)
st.map(MapData)