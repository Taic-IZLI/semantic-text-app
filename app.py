import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Заголовок и стиль
st.set_page_config(page_title="Смысловое сравнение текстов", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: black;
        color: #39FF14;
        font-family: 'Courier New', monospace;
    }
    .matrix {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: -1;
        background: radial-gradient(circle, rgba(0,0,0,1) 0%, rgba(1,20,9,1) 100%);
    }
    .header {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        text-shadow: 0 0 10px #0f0;
    }
    .panel {
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        border: 1px solid #0f0;
        border-radius: 15px;
        box-shadow: 0 0 20px #0f0;
    }
    </style>
    <div class="matrix"></div>
    <div class="header">🌐 Сравнение смыслов текстов (русский язык)</div>
    """,
    unsafe_allow_html=True
)

with st.container():
    with st.expander("ℹ️ Как пользоваться приложением?", expanded=False):
        st.markdown("""
        1. Введите два текста на русском языке.
        2. Нажмите кнопку **Сравнить**.
        3. Получите процент смыслового сходства и оценку.
        """)

# Загружаем модель
@st.cache_resource
def load_model():
    return SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

model = load_model()

# Интерфейс
with st.container():
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    text1 = st.text_area("📝 Текст 1", height=150)
    text2 = st.text_area("📝 Текст 2", height=150)

    if st.button("Сравнить"):
        if not text1.strip() or not text2.strip():
            st.warning("Пожалуйста, введите оба текста.")
        else:
            emb1 = model.encode(text1, convert_to_tensor=True)
            emb2 = model.encode(text2, convert_to_tensor=True)

            similarity = util.cos_sim(emb1, emb2).item()
            percent = similarity * 100

            if percent >= 85:
                verdict = "🔷 Тексты почти идентичны по смыслу."
            elif percent >= 60:
                verdict = "🟡 Тексты частично похожи по смыслу."
            else:
                verdict = "🔴 Смыслы текстов разные."

            st.success(f"**Сходство по смыслу: {percent:.2f}%**")
            st.markdown(f"**{verdict}**")

    st.markdown('</div>', unsafe_allow_html=True)
