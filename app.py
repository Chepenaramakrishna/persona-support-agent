import streamlit as st
from src.classifier import classify_customer_persona

st.title("Persona Adaptive Customer Support Agent")

user_input = st.text_area("Enter Customer Message")

if st.button("Analyze"):

    persona = classify_customer_persona(user_input)

    st.success(f"Detected Persona: {persona}")

    st.write("Customer Message:")
    st.write(user_input)