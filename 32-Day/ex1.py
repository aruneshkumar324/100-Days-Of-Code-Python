import datetime as dt
import smtplib
from random import choice


now = dt.datetime(year=2022, month=1, day=20)
weekday = now.weekday()

sender_email = "pythonemailtesting76@gmail.com"
password = "9534857622"


if weekday == 3:
    with open('quotes.txt', "r") as quotes_file:
        quotes_list = quotes_file.readlines()
        print(quotes_list)
        today_quote = choice(quotes_list)
        print(today_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs="pythonemailtesting76@yahoo.com",
            msg=f"Subject:Quotes\n\n{today_quote}"
        )
