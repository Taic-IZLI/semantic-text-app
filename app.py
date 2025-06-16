import streamlit as st
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

st.set_page_config(page_title="Сравнение смыслов", layout="wide")
st.markdown("""
    <style>
    body {
        background: black;
        color: #00FFAA;
        font-family: 'Courier New', monospace;
    }
    .matrix {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        background: black;
        overflow: hidden;
    }
    .header {
        background-color: rgba(0,0,0,0.7);
        padding: 1rem;
        border-bottom: 2px solid #00FFAA;
        text-align: center;
        font-size: 24px;
        color: #00FFAA;
    }
    .sidebar-content {
        padding: 1rem;
        background-color: rgba(0, 0, 0, 0.7);
        color: #00FFAA;
    }
    </style>
    <div class="matrix"></div>
    <div class="header">Введите два текста для сравнения по смыслу</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
        <div class="sidebar-content">
        <h3>Инструкция</h3>
        <p>Введите два текста в поля. Нажмите "Сравнить". Вы увидите процентное сходство по смыслу.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    input, textarea {
        background-color: #001F1F !important;
        color: #00FFAA !important;
        border: 1px solid #00FFAA !important;
    }
    </style>
""", unsafe_allow_html=True)

tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    hidden_state = outputs.last_hidden_state
    attention_mask = inputs.attention_mask.unsqueeze(-1).expand(hidden_state.shape).float()
    masked_state = hidden_state * attention_mask
    summed = torch.sum(masked_state, dim=1)
    counted = torch.clamp(attention_mask.sum(dim=1), min=1e-9)
    mean_pooled = summed / counted
    return mean_pooled[0].numpy()

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

text1 = st.text_area("Текст 1")
text2 = st.text_area("Текст 2")

if st.button("Сравнить"):
    if text1 and text2:
        vec1 = get_embedding(text1)
        vec2 = get_embedding(text2)
        similarity = cosine_similarity(vec1, vec2) * 100

        if similarity > 90:
            result = "Тексты идентичны по смыслу."
        elif similarity > 60:
            result = "Тексты похожи по смыслу."
        elif similarity > 30:
            result = "Тексты имеют слабое смысловое сходство."
        else:
            result = "Тексты не похожи по смыслу."

        st.markdown(f"""
            <div style='padding: 1rem; background: rgba(0, 255, 170, 0.1); border-left: 4px solid #00FFAA;'>
            <b>Сходство по смыслу:</b> {similarity:.2f}%<br>
            <i>{result}</i>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Пожалуйста, введите оба текста.")
