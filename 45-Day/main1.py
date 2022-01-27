from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
news_page = response.text


soup = BeautifulSoup(news_page, 'html.parser')
print(soup.title.getText())

# storyLink = soup.select_one(selector="td .titlelink")
article_title = soup.find(name='a', class_='titlelink')
print(article_title.getText())

article_link = article_title.get('href')
print(article_link)

article_score = soup.find(name='span', class_='score')
print(article_score.getText())


titles = []
links = []

for x in soup.find_all(name='a', class_='titlelink'):
    titles.append(x.getText())
    links.append(x.get('href'))

print(titles)
print(links)

points = [int(value.getText().split()[0]) for value in soup.find_all(name='span', class_='score')]
print(points)

print(max(points))

hight_points = points.index(max(points))
print(hight_points)

print(titles[hight_points])
print(links[hight_points])












