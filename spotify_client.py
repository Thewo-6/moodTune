
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def get_spotify_client():
    client_id = "2d001754fc024edf89c27ee0bc812eb9"
    client_secret = "0e44a6b91fc64ac3aef01e328be58449"
    auth_manager = SpotifyClientCredentials(client_id, client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)
