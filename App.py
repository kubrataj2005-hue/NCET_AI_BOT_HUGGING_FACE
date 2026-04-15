import streamlit as st
from transformers import pipeline

#load the summarization model
@st.cache_resource
def load_summarize():
  return pipeline("summerization",model="sshleifer/distilbart-cnn-12-6")
