import streamlit as st
st.header("welcome to streamlit")
name=st.text_input("Enter your name")
st.button("Submit", on_click=lambda: st.write(f"Hello, {name}! Welcome to Streamlit!"))

import pandas as pd
file=st.file_uploader("upload csv file",type="csv")
if file:
    df=pd.read_csv(file)
    st.write(df)
    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)