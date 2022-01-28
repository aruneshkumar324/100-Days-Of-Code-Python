import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

link = "https://www.amazon.com/dp/B072NFGLSV/ref=syn_sd_onsite_desktop_258?psc=1&pd_rd_plhdr=t&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUFdRVkFYVFREN1AxJmVuY3J5cHRlZElkPUEwMTQyMTI4M1RZQkZMMFdIM1hYNCZlbmNyeXB0ZWRBZElkPUEwNDk4ODMxUUpCODRUU0VIWkQ0JndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
HEADERS = {
        "User-Agent": "Defined",
        "Accept-Language": "en-US,en;q=0.5"
    }

# AMAZON PRICE
response = requests.get(url=link, headers=HEADERS)
amazon_response = response.text


#   SCRAPING
soup = BeautifulSoup(amazon_response, 'html.parser')

# current_price = soup.select_one(selector=".a-offscreen")
# print(current_price.getText())

title = soup.find(name="span", id="productTitle")
product_title = title.getText().strip()

current_price = soup.find(name="span", class_="a-offscreen")
# price = float(current_price.getText().split("$")[1])

price = 250


# EMAIL
MY_EMAIL = "pythonemailtesting76@gmail.com"
PASSWORD = "9534857622"

if price <= 300:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="pythonemailtesting76@yahoo.com",
            msg=f"Subject:Price Alert\n\n{product_title} is now ${price}\n{link}"
        )
else:
    print("Price Still Not Decrease")

