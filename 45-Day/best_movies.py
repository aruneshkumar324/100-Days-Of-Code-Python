import requests
from bs4 import BeautifulSoup


movies_response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response = movies_response.text


soup = BeautifulSoup(response, 'html.parser')

title = soup.find_all(name='h3', class_='title')

titles = []
for x in title[::-1]:
    titles.append(x.getText())

# titles = [value.getText() for value in title[::-1]]
# print(titles)

with open('movies.txt', mode='a') as movies_title:
    for x in titles:
        movies_title.write(f"{x}\n")
