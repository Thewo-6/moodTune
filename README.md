# 🎧 MoodTune – AI Mood-Based Music Recommender (Multimodal Version)

**MoodTune** is an AI-powered web app that detects your mood using either natural language (text) or facial expressions (image), and recommends music from Spotify to match or lift your emotional state.

---

## 💡 Features

- 🤖 **Text-based emotion detection** using a fine-tuned BERT model
- 📸 **Facial emotion detection** using DeepFace and your webcam or uploaded selfies
- 🎵 **Spotify integration** to fetch and recommend songs that match or lift your mood
- ✅ User-friendly interface built with **Streamlit**

---

## 🏗️ Project Structure

moodtune_multimodal/
├── app_multimodal.py # Main Streamlit UI (text + image)
├── mood_detection.py # Text emotion classifier
├── face_emotion_detector.py # Face-based emotion detector
├── song_recommender_spotify.py # Recommends tracks using Spotify API
├── spotify_client.py # Spotify Web API connection logic
├── requirements.txt # List of dependencies
└── README.md # You're here!



🐍 Python Environment Setup
To ensure full compatibility with all libraries (especially deepface, torch, and streamlit), we recommend the following setup:

✅ Recommended Python Version
Python 3.9 or 3.10

⚠️ deepface may not work reliably with Python 3.11 or 3.12 in some environments due to dependency mismatches (e.g., tensorflow, keras, opencv, retinaface).


Create and Activate a Virtual Environment

Using venv (standard):
python3.10 -m venv moodtune-env
source moodtune-env/bin/activate  # For macOS/Linux
# or
.\moodtune-env\Scripts\activate   # For Windows



Or using conda:
conda create -n moodtune-env python=3.10
conda activate moodtune-env


Once inside the environment, run:
pip install -r requirements.txt
