import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Смысловое сравнение текста", layout="wide", page_icon="🧠")

with open("assets/futuristic.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("assets/background.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=0, width=0)

st.markdown('<div id="main-section" class="main-title">Смысловое сравнение текста</div>', unsafe_allow_html=True)

st.markdown('<div class="neon-card">', unsafe_allow_html=True)
text1 = st.text_area("🔹 Введите первый текст", height=160)
text2 = st.text_area("🔸 Введите второй текст", height=160)
if st.button("Сравнить смысл", type="primary"):
    st.success("Сравнение ещё не подключено, но всё готово! 🧠")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="instructions"></div>', unsafe_allow_html=True)
with st.expander("📘 Как пользоваться приложением?", expanded=False):
    st.markdown("""
    1. Введите два текста для сравнения.  
    2. Нажмите кнопку **Сравнить смысл**.  
    3. Программа покажет, насколько тексты похожи по смыслу (функция добавляется далее).
    """)

st.markdown('<div id="examples"></div>', unsafe_allow_html=True)
with st.expander("🧪 Примеры для теста", expanded=False):
    st.markdown("""
    **Пример 1**  
    Текст 1: Я люблю изучать искусственный интеллект.  
    Текст 2: Мне нравится заниматься ИИ и машинным обучением.

    **Пример 2**  
    Текст 1: Сегодня хорошая погода.  
    Текст 2: Завтра будет солнечно и тепло.
    """)
