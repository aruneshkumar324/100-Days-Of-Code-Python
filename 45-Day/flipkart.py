import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DLG&otracker=nmenu_sub_TVs%20%26%20Appliances_0_LG")
flipkart_response = response.text


soup = BeautifulSoup(flipkart_response, 'html.parser')
print(soup.title.getText())


product_title = soup.find_all(name='div', class_='_4rR01T')

# TITLE
titles = []
for x in product_title:
    titles.append(x.getText())

print(titles)
print(len(titles))
print(titles[-1])


#   PRODUCT IMAGES
images = soup.find_all(name='img', class_='_396cs4 _3exPp9')

# with all atributes
all_image = []

# with image link only
all_image_link = []

for x in images:
    all_image.append(x)
    all_image_link.append(x.get('src'))

print(all_image)
print(all_image_link)






















