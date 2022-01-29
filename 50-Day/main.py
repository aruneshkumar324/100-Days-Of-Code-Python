from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


EMAIL = "0786indianking@gmail.com"
PASSWORD = "9534857622"

path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get(url="https://tinder.com/")
time.sleep(2)

# loging button
login = driver.find_element_by_xpath('//*[@id="t-48487324"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(2)

# fb window open for login
fb_login = driver.find_element_by_xpath('//*[@id="t-1776868400"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
time.sleep(2)


# access new window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


fb_email = driver.find_element_by_xpath('//*[@id="email"]')
fb_email.send_keys(EMAIL)

fb_password = driver.find_element_by_xpath('//*[@id="pass"]')
fb_password.send_keys(PASSWORD)
fb_password.send_keys(Keys.ENTER)


# BACK TO FIRST WINDOW
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

location_allow = driver.find_element_by_xpath('//*[@id="t-1776868400"]/div/div/div/div/div[3]/button[1]')
location_allow.send_keys(Keys.ENTER)

time.sleep(2)

cookies_allow = driver.find_element_by_xpath('//*[@id="t-48487324"]/div/div[2]/div/div/div[1]/button')
cookies_allow.send_keys(Keys.ENTER)

time.sleep(2)

notification = driver.find_element_by_xpath('//*[@id="t-1776868400"]/div/div/div/div/div[3]/button[2]')
notification.send_keys(Keys.ENTER)

time.sleep(2)

# like profile
for _ in range(5):
    time.sleep(1)

    try:
        print('called')
        like = driver.find_element_by_xpath('//*[@id="t-48487324"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like.send_keys(Keys.ENTER)

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)












