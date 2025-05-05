import streamlit as st
from pathlib import Path
import subprocess

st.set_page_config(page_title="olmocr Demo", layout="wide")

st.title("olmOCR PDF Parser")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded. Starting processing...")

    # Save PDF to local file
    input_dir = Path("input_pdfs")
    input_dir.mkdir(exist_ok=True)
    pdf_path = input_dir / uploaded_file.name
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Run olmocr pipeline (this is GPU-intensive)
    try:
        subprocess.run(
            ["python", "-m", "olmocr.pipeline", "workspace", "--pdfs", str(pdf_path)],
            check=True
        )
        output_file = Path("workspace/results") / f"output_{uploaded_file.name}.jsonl"
        if output_file.exists():
            st.success("Processing complete. Extracted text:")
            with open(output_file) as f:
                st.code(f.read(), language="json")
        else:
            st.error("Processing failed or output not found.")
    except Exception as e:
        st.error(f"Error running olmocr pipeline: {e}")
