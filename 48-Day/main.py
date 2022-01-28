from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(url="https://www.flipkart.com/")

# driver.get("https://www.amazon.in/HP-Pavilion-15-6-inch-Graphics-15-dk1514TX/dp/B09DY8BGSY?ref_=Oct_DLandingS_D_edd4b02d_63&smid=A14CZOWI0VEHLG")
# price = driver.find_element_by_id("productTitle")
# print(price.text)

driver.get("https://www.google.com/")

google = driver.find_element_by_name("q")

print(google.tag_name)
print(google.get_attribute("class"))
print(google.get_attribute("maxlength"))
print(google.get_attribute("data-ved"))
print(google.size)

# google_css = driver.find_element_by_css_selector("#SIvCob a")
google_css = driver.find_elements_by_css_selector("#SIvCob a")
for x in google_css:
    print(x.text)


google_xpath = driver.find_element_by_xpath('//*[@id="SIvCob"]/a[1]')

print(google_xpath.text)
























# driver.close()
driver.quit()