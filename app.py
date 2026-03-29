import streamlit as st
import pandas as pd

st.title("Language Translator")

# تحميل البيانات (مع تحديث تلقائي)
@st.cache_data
def load_data():
    return pd.read_csv("words.csv")

df = load_data()

# تنظيف البيانات مرة وحدة
df['English'] = df['English'].astype(str).str.strip().str.lower()
df['Arabic'] = df['Arabic'].astype(str).str.strip()

# اختيار الاتجاه
option = st.radio(
    "Choose translation direction:",
    ("English → Arabic", "Arabic → English")
)

# إدخال المستخدم
user_input = st.text_input("Enter a word:")

# زر الترجمة
if st.button("Translate"):

    if user_input.strip() == "":
        st.warning("Please enter a word")
    else:

        # تنظيف الإدخال
        clean_input = user_input.strip().lower()

        if option == "English → Arabic":
            result = df[df['English'] == clean_input]

            if not result.empty:
                st.success(result['Arabic'].values[0])
            else:
                st.error("Word not found")

        else:
            clean_input = user_input.strip()
            result = df[df['Arabic'] == clean_input]

            if not result.empty:
                st.success(result['English'].values[0])
            else:
                st.error("Word not found")

# زر تحديث (حل إضافي)
if st.button(" Refresh Data"):
    st.cache_data.clear()
    st.rerun()
