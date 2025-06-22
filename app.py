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
  50% {background
