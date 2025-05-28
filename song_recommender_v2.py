import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

# Replace these with your actual credentials
SPOTIFY_CLIENT_ID = "174b3fa8a5d84d959a7e005e476d14ee"
SPOTIFY_CLIENT_SECRET = "dc297df961cb4295aea55a43f44e41fd"

# Spotify authentication
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Mood-based recommendation
def recommend_from_spotify(emotion, limit=3, open_links=True):
    results = sp.search(q=emotion, type="track", limit=limit)
    recommendations = []
    print(f"🔍 Searching Spotify for: {emotion}")
                
    for item in results['tracks']['items']:
        name = item['name']
        artist = item['artists'][0]['name']
        
        full_song_url = item['external_urls']['spotify']  # 👈 this is the full song link

        print