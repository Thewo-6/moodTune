
from spotify_client import get_spotify_client
import random

def recommend_spotify_tracks(emotion, num_songs=3):
    spotify = get_spotify_client()
    search_query = f"{emotion} music"
    results = spotify.search(q=search_query, type='track', limit=20)
    tracks = results['tracks']['items']
    selected = random.sample(tracks, k=min(num_songs, len(tracks)))

    return [{
        "title": t['name'],
        "artist": t['artists'][0]['name'],
        "url": t['external_urls']['spotify']
    } for t in selected]
