from selenium import webdriver


path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)
driver.get(url="https://www.python.org/")


time = driver.find_elements_by_css_selector(".event-widget li time")
title = driver.find_elements_by_css_selector(".event-widget li a")

# ANGELA SOLUTION
events = {}

for x in range(len(time)):
    events[x] = {
        "times": time[x].text,
        "name": title[x].text
    }

print(events)

#   #  MY SOLUTION
# times = []
# events = []
# [times.append(x.text) for x in time]
# [events.append(x.text) for x in title]
# data = {}
# for (x, y) in enumerate(times):
#     data.update({x: {"time": times[x], "name": events[x]}})
#
# print(data)



driver.quit()