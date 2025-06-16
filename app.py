import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Загружаем улучшенную модель
model = SentenceTransformer('paraphrase-MiniLM-L12-v2')

st.set_page_config(page_title="Сравнение смыслов", layout="wide")

# Стили + JS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<canvas id="background"></canvas>
<script src="assets/background.js"></script>
<script src="assets/sidebar.js"></script>
""", unsafe_allow_html=True)

# Шапка
st.markdown("<h1 class='main-title'>💡 Сравнение смыслов между текстами</h1>", unsafe_allow_html=True)

# Инструкция
st.markdown("""
<div class='instructions'>
<b>Как пользоваться:</b><br>
1. Введите два текста или предложения<br>
2. Нажмите кнопку сравнения<br>
3. Получите процент сходства и вывод — идентичны или нет<br>
</div>
""", unsafe_allow_html=True)

# Ввод текстов
col1, col2 = st.columns(2)
with col1:
    text1 = st.text_area("Текст 1", height=200)
with col2:
    text2 = st.text_area("Текст 2", height=200)

# Кнопка и результат
if st.button("🚀 Сравнить тексты"):
    if text1 and text2:
        emb1 = model.encode(text1, convert_to_tensor=True)
        emb2 = model.encode(text2, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(emb1, emb2).item()
        percent = round(similarity * 100, 2)

        if percent > 90:
            verdict = "🟢 Идентичны по смыслу"
        elif percent > 60:
            verdict = "🟡 Похожи по смыслу"
        else:
            verdict = "🔴 Отличаются по смыслу"

        st.markdown(f"""
        <div class='result-box'>
            <h2>{verdict}</h2>
            <p><b>Сходство по смыслу:</b> {percent}%</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Введите оба текста для сравнения.")
