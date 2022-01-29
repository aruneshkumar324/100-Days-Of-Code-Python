from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

total = driver.find_element_by_css_selector("#articlecount a")
print(total.text)
# total.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()


search = driver.find_element_by_name(name="search")

search.send_keys("Arunesh")
search.send_keys(Keys.ENTER)

# driver.quit()