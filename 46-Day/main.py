import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}/")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/2000-08-12/")
songs_response = response.text


soup = BeautifulSoup(songs_response, 'html.parser')

songs_title = soup.find_all(name="h3", id="title-of-a-story")

songs = []
for x in songs_title[6::2]:
    songs.append(x.getText().split('\n'))

list_songs = []
for song in songs[::2]:
    list_songs.append(song[1])


# SPOTIFY

CLIENT_ID = "f57de8bd23b24aeea99799dcb92d8510"
CLIENT_SECRET = "1ddf6a8ce423492789ec83a3251c9edd"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://www.billboard.com/charts/hot-100/2000-08-12/",
        scope="user-library-read",
        cache_path='.cache',
        show_dialog=True
    )
)

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# 3 STEP
user_id = sp.current_user()["id"]
date = "2000-08-12"
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



# 4 STEP


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)








































