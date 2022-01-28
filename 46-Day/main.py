import requests
from bs4 import BeautifulSoup

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}/")
songs_response = response.text


soup = BeautifulSoup(songs_response, 'html.parser')

songs_title = soup.find_all(name="h3", id="title-of-a-story")

songs = []

for x in songs_title[6::2]:
    songs.append(x.getText().split('\n'))


for song in songs[::2]:
    print(song[1])


# 2000-08-12