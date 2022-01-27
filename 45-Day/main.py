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

print(soup.find_all(name='li'))

all_link = soup.find_all('a')
for link in all_link:
    print(link.get('href'))
    # print(link.getText())


print()
print()

paragraph = soup.find(name='p', class_='about')
print(paragraph)
print(paragraph.getText())
print(paragraph.string)
print(paragraph.name)
print(paragraph.get('class'))


heading = soup.find(name='h1', id='name')
print(heading)

compuny_url = soup.select_one(selector='p a')
print(compuny_url)
print(compuny_url.getText())
print(compuny_url.get('href'))


heading = soup.select(selector='.heading')
# heading = soup.select_one(selector='.heading')
print(heading)
























