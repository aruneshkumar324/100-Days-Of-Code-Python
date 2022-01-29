from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


USERNAME = "pythonemailtesting76@gmail.com"
UN = "python_boat"
PASSWORD = "9534857622"
DOWNLOAD_SPEED = 75
UPLOAD_SPEED = 75


path = "C:\Development\chromedriver.exe"

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed.click()

        sleep(60)

        self.down_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/i/flow/login")
        sleep(2)
        username_field = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        username_field.send_keys(USERNAME)
        sleep(1)
        username_field.send_keys(Keys.ENTER)

        sleep(2)
        verify = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        verify.send_keys(UN)
        sleep(1)
        verify.send_keys(Keys.ENTER)

        sleep(2)
        password_field = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(PASSWORD)
        sleep(1)
        password_field.send_keys(Keys.ENTER)
        sleep(5)

        write_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message = f"Hey Internet Provider, why is my internet speed {self.down_speed}down/{self.upload_speed}up, when i pay for {DOWNLOAD_SPEED}down/{UPLOAD_SPEED}/up?"
        print(message)
        write_tweet.send_keys(message)

        sleep(3)

        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()



bot = InternetSpeedTwitterBot(path)

bot.get_internet_speed()
bot.tweet_at_provider()
















