from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get(url="https://www.appbrewery.co/p/newsletter")

signup = driver.find_element_by_name(name="email")

signup.send_keys('arunesh@gmail.com')
signup.send_keys(Keys.ENTER)
