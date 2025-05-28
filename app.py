import streamlit as st
from mood_detection import detect_emotion
from song_recommender import recommend_songs

# === Page Setup ===
st.set_page_config(page_title="MoodTune", layout="centered")
st.title("🎧 MoodTune")
st.subheader("Tell us how you feel. We'll suggest songs for your mood 🎶")

# === Emotion & Mood Mappings ===
EMOTION_MAP = {
    "joy": "happy", "happiness": "happy", "sadness": "sad", "grief": "sad",
    "anger": "angry", "disgust": "angry", "love": "romantic", "neutral": "calm",
    "surprise": "energetic", "fear": "sad", "confident": "confident"
}

COUNTER_MOOD = {
    "sad": "happy", "angry": "calm", "fear": "confident",
    "romantic": "energetic", "confident": "calm", "calm": "energetic",
    "happy": "romantic"
}

MOOD_COLORS = {
    "happy": "#FFF8DC", "sad": "#E0EBF5", "angry": "#FFD6D6", "romantic": "#FFE4E1",
    "confident": "#E6FFE6", "energetic": "#FFFACD", "calm": "#F0FFF0"
}

MOOD_EMOJIS = {
    "happy": "😊", "sad": "😢", "angry": "😡", "romantic": "❤️",
    "confident": "😎", "energetic": "⚡", "calm": "🌿"
}

# === Session Defaults ===
if 'last_songs' not in st.session_state:
    st.session_state['last_songs'] = []
if 'emotion' not in st.session_state:
    st.session_state['emotion'] = ''

# === Get fresh songs based on mood ===
def get_fresh_recommendations(emotion):
    st.session_state['last_songs'] = recommend_songs(emotion)

# === Main App Flow ===
user_input = st.text_input("How are you feeling today?")

if user_input:
    try:
        # Step 1: Detect emotion
        predicted_emotion = detect_emotion(user_input)
        st.success(f"Detected Emotion: {predicted_emotion.capitalize()}")

        # Step 2: User chooses direction
        mood_action = st.radio(
            "What would you like us to do?",
            ("🎭 Match my mood", "☀️ Lift my mood")
        )

        # Step 3: Map emotion to mood
        mapped_emotion = EMOTION_MAP.get(predicted_emotion.lower(), predicted_emotion.lower())
        if mood_action == "☀️ Lift my mood":
            mapped_emotion = COUNTER_MOOD.get(mapped_emotion, mapped_emotion)

        # Step 4: Save + fetch songs
        st.session_state['emotion'] = mapped_emotion
        get_fresh_recommendations(mapped_emotion)

        # Step 5: Mood card
        bg_color = MOOD_COLORS.get(mapped_emotion, "#F9F9F9")
        mood_icon = MOOD_EMOJIS.get(mapped_emotion, "🎵")

        st.markdown(
            f"""
            <div style="background-color:{bg_color};
                        padding:20px;
                        border-radius:10px;
                        color:#222;
                        font-weight:600;
                        font-size:18px;
                        text-align:center;">
                {mood_icon} Mood Selected: <em>{mapped_emotion.capitalize()}</em>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Step 6: Song list
        st.write("🎵 Recommended Songs:")
        for song in st.session_state['last_songs']:
            st.markdown(f"- **{song['Song']}** by *{song['Artist']}*")

        # Step 7: "Give me more songs" button
        if st.button("🎵 Give me more songs"):
            get_fresh_recommendations(st.session_state['emotion'])
            st.rerun()

    except Exception as e:
        st.error(f"Error: {e}")