import streamlit as st
import torch
from aksara_ocr import AksaraOCR
import matplotlib.pyplot as plt
import numpy as np

st.title("Aksara Jawa App")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

@st.cache_resource
def get_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ocr = AksaraOCR(verbose=True, device=device)
    return ocr

ocr = get_model()

if uploaded_image is not None:
    label, images = ocr.predict(uploaded_image)
    
    fig = plt.figure(figsize=(8, 8))
    columns = 1
    rows = 1
    img = images

    img = img.cpu().numpy()

    img = (img - img.min()) / (img.max() - img.min())
    img = np.array(img * 255.0, dtype=np.uint8)
    fig.add_subplot(rows, columns, 1)
    plt.title(f"label: {label}")
    plt.axis('off')
    plt.imshow(img)
    st.pyplot(fig)