import streamlit as st
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Смысловое сравнение текстов", layout="wide")

# 🔹 Фон с анимацией
st.markdown("""
<style>
body {
  background: #0f0f0f;
  overflow: hidden;
}
#gradient-background {
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
  width: 100vw;
  height: 100vh;
  background: linear-gradient(135deg, #0fffc1, #3c67e3, #0fffc1);
  background-size: 600% 600%;
  animation: gradient 15s ease infinite;
  filter: blur(100px);
  opacity: 0.3;
}
@keyframes gradient {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
</style>
<div id="gradient-background"></div>
""", unsafe_allow_html=True)

# 🔹 Скрипт голосового ввода
st.markdown("""
<script>
function startDictation(id) {
  const textarea = window.parent.document.querySelectorAll("textarea")[id];
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'ru-RU';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;
  recognition.start();

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    textarea.value = transcript;
    textarea.dispatchEvent(new Event('input', { bubbles: true }));
  };

  recognition.onerror = function(event) {
    alert("Ошибка распознавания речи: " + event.error);
  };
}
</script>
""", unsafe_allow_html=True)

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
            <li>Введите или надиктуйте два текста</li>
            <li>Нажмите «Сравнить тексты»</li>
            <li>Система покажет процент смысловой схожести</li>
        </ul>
        <p style='color:#aaa;'>Модель использует нейросети для сравнения смысла фраз.</p>
    </div>
    """, unsafe_allow_html=True)

# 🔹 Заголовок
st.markdown("""
<div class="header">
    <h1>🔍 Сравнение смыслов</h1>
    <p>Сравни тексты и узнай, насколько они близки по смыслу</p>
</div>
""", unsafe_allow_html=True)

# 🔹 Ввод текста с голосом
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='neon-label'>📝 Первый текст</div>", unsafe_allow_html=True)
    st.markdown("<button onclick='startDictation(0)' style='margin-bottom:10px;'>🎙 Ввести голосом</button>", unsafe_allow_html=True)
    text1 = st.text_area("", height=200, placeholder="Введите первый текст...")

with col2:
    st.markdown("<div class='neon-label'>📄 Второй текст</div>", unsafe_allow_html=True)
    st.markdown("<button onclick='startDictation(1)' style='margin-bottom:10px;'>🎙 Ввести голосом</button>", unsafe_allow_html=True)
    text2 = st.text_area("", height=200, placeholder="Введите второй текст...")

# 🔹 Обработка и результат
if st.button("🚀 Сравнить тексты"):
    if text1 and text2:
        emb1 = get_embedding(text1)
        emb2 = get_embedding(text2)
        similarity = cosine_similarity(emb1, emb2)[0][0]
        percent = similarity * 100

        st.markdown(f"""
        <div class="result-box">
            <h2>🧠 Результат:</h2>
            <p>Смысловая схожесть: <span style='color: #00ffcc; font-size: 24px;'>{percent:.2f}%</span></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Пожалуйста, введите оба текста.")
