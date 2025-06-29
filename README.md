# Advancing Video Analytics With AI Agents

This project provides a blueprint for building visually perceptive and interactive AI agents for video search and summarization (VSS) using:
- LLaMA (LLM)
- Pinecone (vector DB)
- Flask (web UI)
- Vision-Language Models (VLM)
- Retrieval-Augmented Generation (RAG)

## Structure
- `app/` — Flask web app
- `video_processing/` — Video frame extraction and preprocessing
- `vlm/` — Vision-language model integration
- `llm/` — LLaMA integration
- `db/` — Pinecone vector DB integration

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app/main.py`
