import streamlit as st

st.title("Himanshu Lodhi Rajput")
st.header("Working on streamlit")
st.subheader("For ChatBot")
st.caption("looking for Junior AI Engineer Job")

code_ex = """
greet_code(name):
    print("Hello",name)
"""
st.code(code_ex, language="python")