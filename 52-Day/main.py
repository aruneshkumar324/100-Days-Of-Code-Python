from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep



EMAIL = "codingstairs@gmail.com"
PASSWORD = "9534857622"

PATH = "C:\Development\chromedriver.exe"


class InstaFollower:
    def __init__(self, driver_path_url):
        self.driver = webdriver.Chrome(executable_path=driver_path_url)

    def login(self):
        self.driver.get(url="https://www.instagram.com/")

        sleep(3)

        username = self.driver.find_element_by_name('username')
        username.send_keys(EMAIL)

        sleep(1)

        password = self.driver.find_element_by_name('password')
        password.send_keys(PASSWORD)

        sleep(2)

        password.send_keys(Keys.ENTER)

        sleep(5)

        not_now = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now.send_keys(Keys.ENTER)

        sleep(2)


    def find_followers(self):
        self.driver.get(url='https://www.instagram.com/chefsteps/')

        sleep(3)

        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(3)

        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(3)


    def follow(self):

        follow_buttons = self.driver.find_elements_by_css_selector('li button')

        for btn in follow_buttons:
            try:
                btn.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(PATH)

bot.login()
bot.find_followers()
bot.follow()




















