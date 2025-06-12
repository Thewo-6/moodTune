# 🎧 MoodTune – AI Mood-Based Music Recommender (Multimodal Version)

**MoodTune** is an AI-powered web app that detects your mood using either natural language (text) or facial expressions (image), and recommends music from Spotify to match or lift your emotional state.

---

## 💡 Features

- 🤖 **Text-based Emotion Detection**  
  Uses a fine-tuned BERT model via Hugging Face Transformers to detect emotions in your input text.

- 📸 **Facial Emotion Recognition**  
  Leverages **DeepFace** with webcam or uploaded images to recognize your current emotional state.

- 🎵 **Spotify Music Recommender**  
  Automatically fetches and recommends music based on your detected mood using the Spotify Web API.

- 🖥️ **Streamlit Frontend**  
  Clean and interactive UI built with Streamlit.

---

## 🏗️ Project Structure

moodtune_multimodal/
├── app_multimodal.py # Main Streamlit app (text + image input)
├── mood_detection.py # Text emotion classifier (HuggingFace)
├── face_emotion_detector.py # Face emotion detector (DeepFace)
├── song_recommender_spotify.py # Music recommender logic
├── spotify_client.py # Spotify API client wrapper
├── requirements.txt # All required dependencies
└── README.md # You're here!


---

## 🐍 Python Environment Setup

> ⚠️ **IMPORTANT:** Use **Python 3.9** or **3.10**.  
> Some dependencies like `deepface`, `tensorflow`, `retinaface`, and `opencv` may not work properly on 3.11+.

### ✅ 1. Create and Activate a Virtual Environment

#### Option 1: Using `venv`

**macOS/Linux:**
```bash
python3.10 -m venv moodtune-env
source moodtune-env/bin/activate

**windows**
py -3.9 -m venv moodtune-env
.\moodtune-env\Scripts\activate

** Install Dependencies
pip install -r requirements.txt


** Running the App
streamlit run app_multimodal.py
