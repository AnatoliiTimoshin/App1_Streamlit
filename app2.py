import streamlit as st

st.title("Інтерактивний веб-додаток")

name = st.text_input("Введіть ваше ім'я:")
if name:
    st.success(f"Привіт, {name}!")

number = st.slider("Виберіть число", 1, 100)
st.write(f"Ви вибрали: {number}")

if st.button("Натисніть мене"):
    st.balloons()