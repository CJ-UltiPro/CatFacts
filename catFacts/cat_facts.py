import streamlit as st
import requests

st.set_page_config(page_title="Cat Facts", page_icon="🐱")

st.title("🐾 Random Cat Fact Generator")

if st.button("Get a Cat Fact"):
    try:
        response = requests.get("https://catfact.ninja/fact")
        response.raise_for_status()
        fact = response.json()["fact"]
        st.success(fact)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.info("Click the button to get a cat fact!")