# Base image with CUDA 12.1 and Ubuntu 22.04
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install Python and system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip git poppler-utils \
    ttf-mscorefonts-installer msttcorefonts \
    fonts-crosextra-caladea fonts-crosextra-carlito \
    gsfonts lcdf-typetools && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    pip install --upgrade pip

# Install olmocr from your fork (replace with your actual GitHub URL)
RUN pip install git+https://github.com/YOUR_USERNAME/olmocr.git@gpu-branch-name#egg=olmocr[gpu] --find-links https://flashinfer.ai/whl/cu124/torch2.4/flashinfer/

# Install Streamlit
RUN pip install streamlit

# Copy your Streamlit app
COPY app.py /app/app.py
WORKDIR /app

# Streamlit runs on port 7860
EXPOSE 7860

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
