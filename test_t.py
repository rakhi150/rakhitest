import streamlit as st

st.title("My First Web App")
st.subheader("Iam so excited")

name = st.text_input("Enter your name:")


if st.button("Greet Me"):
    st.write(f"Hello, {name}! 👋")

numbers = st.slider("Pick a number", 1, 100, 50)

st.write("You selected:", numbers)
