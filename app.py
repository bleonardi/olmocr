import gradio as gr
from olmocr.models.model import make_model
from olmocr.utils.ocr_utils import predict
from PIL import Image
import torchvision.transforms as T

# Load model once
model = make_model()
model.eval()

# Image preprocessing
transform = T.Compose([
    T.Resize((384, 384)),  # Match olmocr expected input size
    T.ToTensor(),
])

def ocr_image(image):
    image = image.convert("RGB")
    img_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    text = predict(model, img_tensor)
    return text

# Gradio interface
demo = gr.Interface(
    fn=ocr_image,
    inputs=gr.Image(type="pil", label="Upload image"),
    outputs="text",
    title="OLMoCR - Optical Layout-Aware OCR",
    description="Upload an image and get OCR text using AllenAI's OLMoCR model.",
)

if __name__ == "__main__":
    demo.launch()
