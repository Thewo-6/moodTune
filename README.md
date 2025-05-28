# 🎧 MoodTune

**MoodTune** is an AI-powered music recommender that suggests songs based on your mood. Simply type how you're feeling, and MoodTune will detect your emotion and recommend 3 songs to either match or lift your mood. Built with 💡 NLP, 🎶 vibes, and 💻 Streamlit.

---

## ✨ Features

- 🤖 Emotion detection using a fine-tuned BERT model (`bert-finetuned-emotion`)
- 🎵 Song recommendations tailored to your mood
- 🎭 Option to match or counterbalance your mood
- 🌈 UI color and emoji themes based on detected emotion
- 🔁 “Give me more songs” button for refreshing recommendations

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/moodtune.git
cd moodtune

2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run the App
streamlit run app.py

# Project Structure
moodtune/
├── app.py                    # Streamlit frontend
├── mood_detection.py        # Emotion classifier
├── song_recommender.py      # Mood → song matcher
├── songs.csv                # Song database
├── requirements.txt         # Dependencies
└── README.md                # This file

