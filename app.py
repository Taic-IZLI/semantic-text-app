import streamlit as st
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Смысловое сравнение текстов", layout="wide")

# Загрузка модели
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased-sentence")
    model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased-sentence")
    return tokenizer, model

tokenizer, model = load_model()

# Функция для получения эмбеддинга
def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()
    return embeddings

# Подключение стилей
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
        emb1 = get_embedding(text1)
        emb2 = get_embedding(text2)
        similarity = cosine_similarity(emb1, emb2)[0][0]
        percent = round(similarity * 100, 2)

        st.markdown(f"""
        <div class="result-box">
            <h2>🧠 Результат:</h2>
            <p>Смысловая схожесть: <span style='color: #00ffcc; font-size: 24px;'>{percent}%</span></p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Пожалуйста, введите оба текста.")
