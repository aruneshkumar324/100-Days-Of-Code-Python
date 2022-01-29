from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Development\chromedriver.exe")
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

total = driver.find_element_by_css_selector("#articlecount a")

print(total.text)

driver.quit()