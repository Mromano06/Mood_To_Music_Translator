from textblob import TextBlob

blob = TextBlob("I feel amazing!");
print(blob.sentiment)



import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = "5f05092321d0497fb3242888b76e7d3d",
    client_secret ="ffabe06efcdf4f7b89d5b4755c1afd7b",
))
