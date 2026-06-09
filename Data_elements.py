import streamlit as st
import pandas as pd

st.title("Kind of Data Elements in Streamlit")

# dataframe section:
st.subheader("Dataframe")
df = pd.DataFrame({
    'Name' : ['Himanshu','Anshu','Shiv'],
    'Age' : [25,22,12]
})
st.dataframe(df)

# Data Editor section:
st.subheader("Editable Dataframe")
st.data_editor(df)


# Table Secton:
st.subheader("Table")
st.table(df)

# Metricz Section:
st.subheader("Matrix")
st.metric(label="Total Strength", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(),1))