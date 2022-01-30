from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = "C:\Development\chromedriver.exe"

class GoogleForm:

    def __init__(self, driver_path_url):
        self.driver = webdriver.Chrome(executable_path=driver_path_url)

    def form(self):
        self.driver.get(url='https://forms.gle/NkMi3dVtSaqED2co9')
        sleep(3)
        property = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        property.send_keys("Property")
        sleep(1)
        price = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys('53')
        sleep(1)
        link = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys('google.com')
        sleep(1)
        button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        button.click()



bot = GoogleForm(PATH)

bot.form()
















PATH = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=PATH)

driver.get(url='https://forms.gle/NkMi3dVtSaqED2co9')
sleep(3)
property = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
property.send_keys("Property")
sleep(1)
price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
price.send_keys('53')
sleep(1)
link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
link.send_keys('google.com')
sleep(1)
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
button.click()





























