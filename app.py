import streamlit as st
import streamlit.components.v1 as components

# Настройка страницы
st.set_page_config(page_title="Text Semantics", layout="wide", page_icon="🤖")

# Подключаем стили
with open("assets/futuristic.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Фон с анимацией
with open("assets/background.html", "r", encoding="utf-8") as f:
    html_bg = f.read()
components.html(html_bg, height=0, width=0)

# Заголовок
st.markdown('<div class="main-title">FUTURE TEXT COMPARATOR</div>', unsafe_allow_html=True)

# Форма
st.markdown('<div class="neon-card">', unsafe_allow_html=True)
text1 = st.text_area("🔹 Введите первый текст", height=160)
text2 = st.text_area("🔸 Введите второй текст", height=160)
if st.button("Сравнить смысл", type="primary"):
    st.success("Функционал добавим на следующем шаге 🚀")
st.markdown('</div>', unsafe_allow_html=True)
