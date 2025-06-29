from transformers import pipeline
from typing import List
import os

# Use OpenAI's GPT-3/4 via Hugging Face pipeline (requires API key)
# You can also use 'gpt2' or 'distilgpt2' for free, local inference
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_captions(captions: List[str]) -> str:
    """Summarize a list of captions using a free Hugging Face model."""
    text = " ".join(captions)
    summary = summarizer(text, max_length=128, min_length=30, do_sample=False)
    return summary[0]['summary_text']
