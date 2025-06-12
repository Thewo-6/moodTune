import pandas as pd
import random

# Load the song dataset
songs_df = pd.read_csv("songs.csv")  # Adjust path if needed

# Song recommendation function
def recommend_songs(emotion, num_songs=3):
    # Filter songs by the emotion (case-insensitive match)
    matching_songs = songs_df[songs_df['Mood'].str.lower() == emotion.lower()]
    
    # If not enough songs, return all available ones
    if len(matching_songs) <= num_songs:
        return matching_songs[['Song', 'Artist']].to_dict(orient='records')
    
    # Randomly select songs from the filtered list
    sampled = matching_songs.sample(n=num_songs)
    return sampled[['Song', 'Artist']].to_dict(orient='records')

# Example usage
if __name__ == "__main__":
    example_emotion = "happy"
    recommendations = recommend_songs(example_emotion)
    for i, song in enumerate(recommendations, 1):
        print(f"{i}. {song['Song']} by {song['Artist']}")