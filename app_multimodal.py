import streamlit as st
from face_emotion_detector import detect_emotion_from_face
from mood_detection import detect_emotion
from song_recommender_spotify import recommend_spotify_tracks
from PIL import Image
import tempfile

st.set_page_config(page_title="🎧 MoodTune", layout="centered")
st.title("🎧 MoodTune")

# 📄 Text Input
st.markdown("### 🖋️ How are you feeling today?")
text_input = st.text_input("Type here if you prefer...", key="typed_text")

# 📸 Facial Mood Detection
st.markdown("## 📷 Facial Mood Detection")

uploaded_image = st.file_uploader("Upload a selfie", type=["jpg", "jpeg", "png"])

picture = st.camera_input("Or take a selfie using your webcam")

emotion = None

if picture or uploaded_image or text_input:
    if picture:
        image_data = picture.getvalue()
        st.image(image_data, caption="📸 Captured Image", width=200)
        emotion = detect_emotion_from_face(image_data)
        st.success(f"Detected Emotion from Face: {emotion}")
    elif uploaded_image:
        image_data = uploaded_image.getvalue()
        st.image(image_data, caption="📸 Uploaded Image", width=200)
        emotion = detect_emotion_from_face(image_data)
        st.success(f"Detected Emotion from Face: {emotion}")
    elif text_input:
        emotion = detect_emotion(text_input)
        st.success(f"Detected Emotion: {emotion}")

    if emotion:
        st.markdown("### 🎯 What would you like us to do?")
        option = st.radio("",
            ["🔴 🧠 Match my mood", "🟡 😊 Lift my mood"],
            index=0)

        final_emotion = emotion
        if option == "🟡 😊 Lift my mood":
            final_emotion = "Happy" if emotion != "Happy" else "Excited"

        st.markdown(f"❤️ Mood Selected: *{final_emotion}*")

        st.markdown("### 🎵 Recommended Songs:")
        recommendations = recommend_spotify_tracks(final_emotion)

        for idx, song in enumerate(recommendations, 1):
            st.markdown(f"{idx}. [{song['title']} by {song['artist']}]({song['url']})")
