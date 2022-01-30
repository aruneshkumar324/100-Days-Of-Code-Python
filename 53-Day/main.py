from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup


BROWSER_HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}

response = requests.get(url='https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-130.10238062183416%2C%22east%22%3A-112.83187280933416%2C%22south%22%3A36.07657154289076%2C%22north%22%3A46.151627970806224%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D', headers=BROWSER_HEADER)

zillow = response.text

soup = BeautifulSoup(zillow, 'html.parser')

price_list = []
address_list = []
links = []

[price_list.append(x.getText().split('/')[0].split('+')[0]) for x in soup.find_all(name="div", class_='list-card-price')]
[address_list.append(x.getText()) for x in soup.find_all(name='address', class_='list-card-addr')]
link_list = []
[link_list.append(x.get('href')) for x in soup.find_all(name='a', class_='list-card-link')]

for x in range(0, 9):
    if link_list[x].startswith("https:"):
        links.append(link_list[x])
    else:
        new_link = 'https://www.zillow.com' + link_list[x]
        links.append(new_link)


# BOT
PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

for x in range(0, 9):
    driver.get(url='https://forms.gle/NkMi3dVtSaqED2co9')
    sleep(3)
    property = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property.send_keys(address_list[x])
    sleep(1)
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(price_list[x])
    sleep(1)
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[x])
    sleep(1)
    button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    button.click()
