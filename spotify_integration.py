import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope="playlist-modify-private"
))

def create_playlist(user_id, playlist_name, playlist_description):
    """Create a new playlist and return its ID."""
    playlist = sp.user_playlist_create(
        user_id,
        name=playlist_name,
        description=playlist_description,
        public=True
    )
    return playlist['id']

def add_tracks_to_playlist(playlist_id, track_uris):
    """Add tracks to the specified playlist."""
    sp.playlist_add_items(playlist_id, track_uris)
