from transformers import BlipProcessor, BlipForConditionalGeneration
from typing import List
import torch
import numpy as np

# Load BLIP model and processor (vision-language model)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def generate_captions(frames: List[np.ndarray]) -> List[str]:
    """
    Generate captions for a list of image frames using BLIP.
    Args:
        frames (List[np.ndarray]): List of image frames (e.g., from OpenCV or PIL, as numpy arrays).
    Returns:
        List[str]: List of generated captions for each frame.
    """
    captions = []
    for frame in frames:
        try:
            inputs = processor(images=frame, return_tensors="pt").to(device)
            with torch.no_grad():
                out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)
            captions.append(caption)
        except Exception as e:
            captions.append(f"[Error generating caption: {e}]")
    return captions
