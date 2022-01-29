from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "pythonemailtesting76@gmail.com"
PASSWORD = "9534857622"


driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

# LOGIN
driver.get(url="https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in")

email_or_phone = driver.find_element_by_name("session_key")
email_or_phone.send_keys(EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# time.sleep(5)

# #   APPLY FOR JOB
# driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=2898789685&f_AL=true&geoId=102713980&keywords=python%20developer&location=India")
#
# #   EASY APPLY
# easy_apply = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
# easy_apply.send_keys(Keys.ENTER)
#
# # FILL PHONE NUMBER
# number = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2898789685,9,phoneNumber~nationalNumber)")
# if number.text == "":
#     number.send_keys('89125436851')
#
#
# submit_btn = driver.find_element_by_css_selector("footer button")
# submit_btn.click()


driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=2894628991&f_AL=true&geoId=102713980&keywords=python%20developer&location=India")

job_list = driver.find_elements_by_css_selector('.jobs-search-results .jobs-search-results__list-item')

for x in job_list:
    x.click()
    time.sleep(2)
    print('Called')
    try:
        #   EASY APPLY
        easy_apply = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
        easy_apply.send_keys(Keys.ENTER)

        # FILL PHONE NUMBER
        number = driver.find_element_by_name(
            "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2898789685,9,phoneNumber~nationalNumber)")
        if number.text == "":
            number.send_keys('89125436851')

        submit_btn = driver.find_element_by_css_selector("footer button")

        if submit_btn.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_btn.click()

        continue
    except NoSuchElementException:
        print('Not Applied')
        continue

time.sleep(5)


















