import gradio as gr
import random
from datasets import load_dataset
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('clip-ViT-B-32')

def fake_gan():
    images = [
        (random.choice(
            [
                "https://upload.wikimedia.org/wikipedia/commons/6/69/NASA-HS201427a-HubbleUltraDeepField2014-20140603.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/7/73/Cycliste_%C3%A0_place_d%27Italie-Paris.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/3/31/Great_white_shark_south_africa.jpg",
            ]
        ), f"label {i}")
        for i in range(3)
    ]
    return images

def search_images_from_text(text):
    emb = model.encode(text)
    return fake_gan()

def search_images_from_image(image):
    image_emb = model.encode(image)
    return fake_gan()

def main():
    text_to_image_iface = gr.Interface(fn=search_images_from_text, inputs="text", outputs="gallery")
    image_to_image_iface = gr.Interface(fn=search_images_from_image, inputs="image", outputs="gallery")
    demo = gr.TabbedInterface([text_to_image_iface, image_to_image_iface], ["Text query", "Image query"])
    demo.launch()
    
if __name__ == "__main__":
    main()
