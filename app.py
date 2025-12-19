import streamlit as st
from PIL import Image, ImageFilter
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Image-to-Image Translation (pix2pix)",
    page_icon="🖼️",
    layout="centered"
)

# ---------------- CUSTOM STYLES ----------------
st.markdown("""
<style>
body {
    background-color: #f6f9ff;
}
.title {
    font-size: 40px;
    font-weight: 700;
    color: #0a2540;
}
.subtitle {
    color: #425466;
    margin-bottom: 25px;
}
.card {
    background: white;
    padding: 24px;
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🖼️ Image-to-Image Translation with cGAN (pix2pix)</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Demonstration of image-to-image translation inspired by pix2pix using edge detection</div>',
    unsafe_allow_html=True
)

# ---------------- CARD START ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 Upload an input image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- IMAGE TRANSFORM FUNCTION ----------------
def pix2pix_transform(image: Image.Image) -> Image.Image:
    """
    Simulates pix2pix-style image-to-image translation
    using edge detection (conditional input → output).
    """
    gray = image.convert("L")
    edges = gray.filter(ImageFilter.FIND_EDGES)
    return edges.convert("RGB")

# ---------------- PROCESS ----------------
if uploaded_file:
    input_image = Image.open(uploaded_file).convert("RGB")

    st.markdown("### 🖼️ Input Image")
    st.image(input_image, use_column_width=True)

    if st.button("✨ Generate Translated Image"):
        with st.spinner("Applying pix2pix-style translation..."):
            output_image = pix2pix_transform(input_image)

        st.success("Image translation complete!")

        st.markdown("### 🎨 Output Image")
        st.image(output_image, use_column_width=True)

# ---------------- CARD END ----------------
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<br><center><small>Task-04 · Image-to-Image Translation · Prodigy Infotech</small></center>",
    unsafe_allow_html=True
)
