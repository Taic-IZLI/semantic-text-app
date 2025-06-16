import streamlit as st
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Стили
st.set_page_config(page_title="Сравнение текстов", layout="wide")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Заголовок и инструкция
st.markdown("<h1 class='main-title'>🔍 Смысловое сравнение текстов</h1>", unsafe_allow_html=True)
st.markdown("""
<div class='instructions'>
<b>Как использовать:</b>
<ul>
<li>Введите два текста</li>
<li>Нажмите "Сравнить"</li>
<li>Вы увидите процент сходства по смыслу</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Фон
st.markdown("""
<script src="assets/background.js"></script>
<canvas id="background"></canvas>
""", unsafe_allow_html=True)

# Ввод текста
text1 = st.text_area("Текст 1", height=150)
text2 = st.text_area("Текст 2", height=150)

# Модель
model = SentenceTransformer('paraphrase-MiniLM-L12-v2')

# Кнопка сравнения
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
        st.warning("Введите оба текста для анализа.")
