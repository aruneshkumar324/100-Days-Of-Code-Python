from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(url="https://www.shoutmeloud.com/contact-us")

name = driver.find_element_by_name("wpforms[fields][0]")
name.send_keys("Fuck You")

email = driver.find_element_by_name("wpforms[fields][1]")
email.send_keys("fuckyou@yahoo.com")

website = driver.find_element_by_name("wpforms[fields][3]")
website.send_keys("https://www.fuckyou.com/")

message = driver.find_element_by_name("wpforms[fields][2]")
message.send_keys(f"I'll Fuck You.\n\n\n\n\n\nThis is BOT Testing")

submit = driver.find_element_by_name("wpforms[submit]")
# submit.send_keys(Keys.ENTER)
submit.click()