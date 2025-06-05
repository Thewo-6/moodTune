
from deepface import DeepFace
from PIL import Image
import numpy as np
from io import BytesIO

def detect_emotion_from_face(uploaded_file):
    if uploaded_file is None:
        return None

    try:
        if isinstance(uploaded_file, bytes):
            img = Image.open(BytesIO(uploaded_file)).convert("RGB")
        else:
            img = Image.open(uploaded_file).convert("RGB")

        analysis = DeepFace.analyze(img_path=np.array(img), actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
        return emotion
    except Exception as e:
        return f"Error: {str(e)}"
