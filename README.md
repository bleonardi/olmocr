# olmOCR Hugging Face Space

> **Note:** this Streamlit prototype requires a GPU host to run olmocr's local
> vision-language model. For a lighter-weight, GPU-free alternative — a FastAPI
> service that calls a hosted vision model instead — see
> [pdf-ocr-api](https://github.com/bleonardi/pdf-ocr-api).

This project is a fork of [olmocr](https://github.com/allenai/olmocr), developed by the Allen Institute for AI (AI2), and modified for use on Hugging Face Spaces.

A GPU-based Hugging Face Space using Docker and Streamlit to demo [olmocr](https://github.com/allenai/olmocr), a PDF-to-text pipeline powered by vision-language models.

## Run Locally (if testing)

```bash
docker build -t olmocr-space .
docker run --gpus all -p 7860:7860 olmocr-space
