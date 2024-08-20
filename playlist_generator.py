from fine_tuning import fine_tune_llama
from online_agent import get_real_time_data
from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
from spotify_integration import create_playlist, add_tracks_to_playlist

class PlaylistGenerator:
    def __init__(self, model_name='fine_tuned_llama'):
        # Load fine-tuned Llama model
        self.model, self.tokenizer = LlamaForCausalLM.from_pretrained(model_name), LlamaTokenizer.from_pretrained(model_name)

    def generate_playlist(self, user_song):
        # Step 1: Get real-time data using online agent
        real_time_songs = get_real_time_data(user_song)

        # Generate playlist name and description
        playlist_name = f"Playlist based on {user_song}"
        playlist_description = "A playlist created based on your favorite song and current trends."

        # Create a playlist and add tracks
        user_id = sp.current_user()['id']
        playlist_id = create_playlist(user_id, playlist_name, playlist_description)

        # Extract track URIs from real-time data
        track_uris = [song['uri'] for song in real_time_songs]  # Adjust this based on your data structure

        # Add tracks to the playlist
        add_tracks_to_playlist(playlist_id, track_uris)

        return playlist_id

if __name__ == "__main__":
    pg = PlaylistGenerator()
    playlist_id = pg.generate_playlist("Song Name")
    print(f"Generated Playlist ID: {playlist_id}")

app.py

from playlist_generator import PlaylistGenerator

def main():
    user_song = input("Enter a song name: ")
    pg = PlaylistGenerator()
    playlist = pg.generate_playlist(user_song)
    print(f"Generated Playlist: {playlist}")

if __name__ == "__main__":
    main()
