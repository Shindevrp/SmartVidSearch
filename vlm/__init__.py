from transformers import BlipProcessor, BlipForConditionalGeneration
from typing import List
import torch

# Load BLIP model and processor (vision-language model)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_captions(frames: List) -> List[str]:
    """Generate captions for a list of frames using BLIP."""
    captions = []
    for frame in frames:
        inputs = processor(images=frame, return_tensors="pt")
        with torch.no_grad():
            out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        captions.append(caption)
    return captions
