import streamlit as st
st.header("welcome to streamlit")
name=st.text_input("Enter your name")
st.button("Submit", on_click=lambda: st.write(f"Hello, {name}! Welcome to Streamlit!"))