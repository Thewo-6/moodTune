from mood_detection_v2 import get_emotion
from song_recommender_v2 import recommend_from_spotify

def mood_to_music():
    # Step 1: Get user input
    user_input = input("🎤 How are you feeling today?\n> ")

    # Step 2: Predict emotion
    emotion = get_emotion(user_input)
    print(f"\n🧠 Detected mood: {emotion}")

    # Step 3: Recommend and open Spotify tracks
    print(f"\n🎵 Recommending songs for mood: {emotion}...")
    songs = recommend_from_spotify(emotion, limit=3, open_links=True)

    # Optional: Show links in console too
    print("\n🎧 Tracks:")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song['Song']} by {song['Artist']}")
        print(f"   🔗 {song['Preview_URL']}")

if __name__ == "__main__":
    mood_to_music()