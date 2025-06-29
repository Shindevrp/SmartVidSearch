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

## Vision-Language Model (VLM) Usage
The `vlm/` module uses BLIP for image captioning, with automatic GPU/CPU device management and robust error handling.

### Example: Generating Captions for Video Frames
```python
import cv2
from vlm import generate_captions

# Example: Extract a frame from a video and generate a caption
cap = cv2.VideoCapture('sample.mp4')
frames = []
ret, frame = cap.read()
if ret:
    frames.append(frame)
cap.release()

captions = generate_captions(frames)
print(captions)
```

- The model will use GPU if available, otherwise CPU.
- Errors during caption generation are caught and reported in the output list.

## Requirements
- For best performance, a CUDA-capable GPU is recommended for BLIP and LLaMA models.
- Ensure your environment has the necessary drivers and libraries for GPU support.
