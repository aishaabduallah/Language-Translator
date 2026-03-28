import streamlit as st
import pandas as pd

st.title("Language Translator")

df = pd.read_csv("words.csv")

option = st.radio("Choose translation direction:", 
                  ("English → Arabic", "Arabic → English"))

user_input = st.text_input("Enter a word:")

if st.button("Translate"):
    if option == "English → Arabic":
        result = df[df['English'].str.lower() == user_input.lower()]
        if not result.empty:
            st.success(result['Arabic'].values[0])
        else:
            st.error("Word not found")

    else:
        result = df[df['Arabic'] == user_input]
        if not result.empty:
            st.success(result['English'].values[0])
        else:
            st.error("Word not found")
