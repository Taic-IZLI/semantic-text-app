import streamlit as st
import streamlit.components.v1 as components

# Настройки страницы
st.set_page_config(
    page_title="Сравнение текстов",
    layout="wide",
    page_icon="🧠",
)

# Вставка HTML-фона
with open("assets/background.html", "r", encoding="utf-8") as f:
    html_code = f.read()
components.html(html_code, height=600, scrolling=False)

# Подключение кастомных стилей
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Заголовок
st.markdown('<div class="title">Сравнение смыслов текстов</div>', unsafe_allow_html=True)

# Основная форма
st.markdown('<div class="card">', unsafe_allow_html=True)
text1 = st.text_area("Первый текст", height=150, key="text1")
text2 = st.text_area("Второй текст", height=150, key="text2")
if st.button("Сравнить"):
    st.success("Сравнение пока не работает. API добавим позже 😉")
st.markdown('</div>', unsafe_allow_html=True)
