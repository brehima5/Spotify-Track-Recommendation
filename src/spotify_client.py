import os
import pandas as pd
import requests
import spotipy
from IPython.display import display
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv(usecwd=True)
loaded = load_dotenv(dotenv_path=dotenv_path)

#print(f"dotenv_loaded={loaded}, dotenv_path={dotenv_path}")



def get_spotify_client():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="http://127.0.0.1:8000/callback",
        scope="playlist-read-private playlist-read-collaborative"
    ))
    return sp


print("Spotify configuration loaded")

sp = get_spotify_client()
