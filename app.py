import streamlit as st

st.set_page_config(page_title="Смысловое сравнение текстов", layout="wide")

# Подключение стилей и скриптов
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Интерфейс
st.markdown("""
<div class="header">
    <h1>🔍 Сравнение смыслов</h1>
    <p>Сравни тексты и узнай, насколько они близки по смыслу</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    text1 = st.text_area("Первый текст", height=200, placeholder="Введите первый текст...")

with col2:
    text2 = st.text_area("Второй текст", height=200, placeholder="Введите второй текст...")

if st.button("🚀 Сравнить тексты"):
    if text1 and text2:
        st.markdown(f"""
        <div class="result-box">
            <h2>🧠 Результат:</h2>
            <p>Здесь будет отображаться степень смысловой близости.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Пожалуйста, введите оба текста.")
