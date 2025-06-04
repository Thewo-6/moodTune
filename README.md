# 🎧 MoodTune – AI Mood-Based Music Recommender

**MoodTune** is an AI-powered web app that detects your mood using natural language and/or facial expressions, and recommends music from Spotify to match or lift your emotional state. Built with 💡 NLP, 🎶 Spotify Web API, and 💻 Streamlit.

## ✨ Features

- 🤖 Emotion detection using a fine-tuned BERT model
- 🧠 (Upcoming) Face-based emotion detection, speech to text based emotion detection
- 🎵 Spotify track recommendations
- 🔗 Clickable links to play songs on Spotify
- Clean and responsive UI

## 🚀 Run the App

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

streamlit run app_spotify.py


moodtune/
├── app_spotify.py              # Streamlit frontend with Spotify integration
├── mood_detection.py           # Emotion classifier using Hugging Face BERT
├── song_recommender_spotify.py # Recommends songs via Spotify API
├── spotify_client.py           # Handles Spotify authentication
├── requirements.txt            # Project dependencies
└── README.md                   # Project overview (this file)
