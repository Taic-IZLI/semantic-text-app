import streamlit as st
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Смысловое сравнение текстов", layout="wide")

# 🔹 Загрузка модели
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased-sentence")
    model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased-sentence")
    return tokenizer, model

tokenizer, model = load_model()

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()
    return embeddings

# 🔹 Стили
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🔹 Боковая панель-инструкция
with st.sidebar:
    st.markdown("""
    <div class="side-panel">
        <h3>ℹ️ Как пользоваться</h3>
        <ul>
            <li>Введите два текст
