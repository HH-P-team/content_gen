import gradio as gr
from transformers import pipeline
from PIL import Image


class Ianalizer:
    def __init__(self):
        self.pipe = pipeline(
            task="image-classification", model="umm-maybe/AI-image-detector"
        )

    def image_classifier(self, image_path):
        query_image = Image.open(image_path)
        return self.pipe(query_image)
