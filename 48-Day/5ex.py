from selenium import webdriver

path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookies = driver.find_element_by_id("cookie")


for _ in range(1000000):
    cookies.click()