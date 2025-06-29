import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template, jsonify
from video_processing import extract_frames, preprocess_frame
from vlm import generate_captions
from llm import summarize_captions
from db import upsert_embeddings, query_embedding
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load embedding model (using sentence-transformers as a placeholder for llama-text-embed-v2)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Replace with llama-text-embed-v2 if available

@app.route('/', methods=['GET'])
def index():
    return 'Video Analytics AI Agent — Home'

@app.route('/analyze', methods=['POST'])
def analyze_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    video = request.files['video']
    video_path = f"/tmp/{video.filename}"
    video.save(video_path)

    # 1. Extract and preprocess frames
    frames = extract_frames(video_path, frame_rate=1)
    processed_frames = [preprocess_frame(f) for f in frames]

    # 2. Generate captions for frames
    captions = generate_captions(processed_frames)

    # 3. Summarize captions using BART (OpenAI-free model)
    summary = summarize_captions(captions)

    # 4. Generate embeddings for captions
    embeddings = embedding_model.encode(captions)
    ids = [f"frame_{i}" for i in range(len(captions))]
    upsert_embeddings(embeddings, ids)

    return jsonify({
        'summary': summary,
        'captions': captions
    })

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    embedding = embedding_model.encode([query])[0]
    results = query_embedding(embedding)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
