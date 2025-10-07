import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from textblob import TextBlob

blob = TextBlob("I feel amazing!");
print(blob.sentiment)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = "5f05092321d0497fb3242888b76e7d3d",
    client_secret ="ffabe06efcdf4f7b89d5b4755c1afd7b",
))
results = sp.search(q="chill playlist", type="playlist", limit=1)
print(results['playlists']['items'][0]['name'])