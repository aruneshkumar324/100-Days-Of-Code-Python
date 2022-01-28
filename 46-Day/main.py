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

# for song in songs[::2]:
#     print(song[1])


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















































