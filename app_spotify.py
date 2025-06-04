
import streamlit as st
from mood_detection import detect_emotion
from song_recommender_spotify import recommend_spotify_tracks

st.set_page_config(page_title="MoodTune", layout="centered")

st.title("🎧 MoodTune")
st.write("Tell us how you feel. We'll suggest songs for your mood 🎶")

user_input = st.text_input("How are you feeling today?")

if user_input:
    emotion = detect_emotion(user_input)
    st.success(f"Detected Emotion: {emotion.capitalize()}")

    mood_action = st.radio("What would you like us to do?",
                           ["🧠 Match my mood", "🌞 Lift my mood"])

    if mood_action:
        st.markdown(f"❤️ Mood Selected: *{emotion.capitalize()}*")

        recommendations = recommend_spotify_tracks(emotion)

        st.subheader("🎵 Recommended Songs:")
        for i, song in enumerate(recommendations, 1):
            st.markdown(f"{i}. **[{song['title']} by {song['artist']}]({song['url']})**")
