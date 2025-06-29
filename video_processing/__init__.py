import cv2
from typing import List

def extract_frames(video_path: str, frame_rate: int = 1) -> List:
    """Extract frames from a video at a specified frame rate (frames per second)."""
    frames = []
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps // frame_rate) if fps > 0 else 1
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval == 0:
            frames.append(frame)
        count += 1
    cap.release()
    return frames

def preprocess_frame(frame):
    """Resize and normalize frame for model input."""
    resized = cv2.resize(frame, (224, 224))
    normalized = resized / 255.0
    return normalized
