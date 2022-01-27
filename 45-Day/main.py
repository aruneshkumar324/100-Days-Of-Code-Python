from bs4 import BeautifulSoup

with open('website.html', encoding='UTF8') as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')

# print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.h1)
print(soup.h1["id"])
print(soup.h1.string)

print(soup.find_all('li'))

all_link = soup.find_all('a')
for link in all_link:
    print(link.get('href'))
