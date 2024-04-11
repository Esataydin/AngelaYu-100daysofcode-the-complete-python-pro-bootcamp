from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import requests


spotify_id: str = YOUR_SPOTIFY_ID
spotify_client_secret: str = YOUR_SPOTIFY_CLIENT_SECRET

date: str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url: str = f"https://www.billboard.com/charts/hot-100/{date}/"
data: str = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")
titles = soup.select(selector="ul li h3")
title_texts = [title.getText().replace("\n", "").replace("\t", "") for title in titles]
del title_texts[100:]

# Spotify authentication with given scope, Modifying playlists in our example.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        # You must use your Spotify API credenticals in token.txt
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in title_texts:
    # searches and finds musics by name and year
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        # gets Spotify "uri" and appends it to song_uris list if song is listed on Spotify. Prints exception otherwise.
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

