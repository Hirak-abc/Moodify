from flask import Flask, request, jsonify, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Mood to Genre Map
mood_genre_map = {
    "Happy": "Pop",
    "Sad": "Acoustic",
    "Energetic": "Dance",
    "Relaxed": "Chill",
    "Romantic": "R-n-B",
    "Angry": "Metal",
    "Melancholy": "Blues",
    "Motivated": "Hip-Hop",
    "Thoughtful": "Jazz",
    "Calm": "Ambient",
    "Nostalgic": "Classic rock",
    "Excited": "Electronic",
    "Peaceful": "Classical",
    "Confident": "Funk",
    "Lonely": "Indie",
    "Hopeful": "Gospel",
    "Playful": "Ska",
    "Dreamy": "Dream pop",
    "Anxious": "Lo-fi",
    "Bold": "Punk"
}

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="2a63c5236abd42aa8dd311277244540a",
    client_secret="daf869a9ecd547e38a046fac42886dd0"
))

@app.route("/")
def root_redirect():
    return redirect("/home")

@app.route("/home")
def home():
    return app.send_static_file("index.html")

@app.route("/songs", methods=["POST"])
def get_songs():
    # Get the mood from the form and maintain its case
    mood = request.form.get("mood", "")
    if not mood:
        return jsonify({"error": "Please provide a mood parameter in 'mood' form data."}), 400

    # Look up the genre in the dictionary
    genre = mood_genre_map.get(mood, "pop")

    results = sp.search(q=f'genre:"{genre}"', type="track", limit=50)
    tracks = results["tracks"]["items"]

    songs = []
    for t in tracks:
        song_info = {
            "name": t["name"],
            "artist": ", ".join([artist["name"] for artist in t["artists"]]),
            "album": t["album"]["name"],
            "spotify_url": t["external_urls"]["spotify"]
        }
        songs.append(song_info)

    return jsonify({"mood": mood, "genre": genre, "songs": songs})

if __name__ == "__main__":
    app.run(debug=True)