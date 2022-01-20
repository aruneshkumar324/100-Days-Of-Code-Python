import datetime as dt
import pandas as pd
import smtplib
from random import choice


# GET CURRENT DATE
now = dt.datetime.now()
print(now)

year = now.year
month = now.month
day = now.day


#   CSV FILE DATA
data = pd.read_csv('birthdays.csv')


try:
    today_bod = data[data["day"] == day]
    print(today_bod)

    bod_data = today_bod.to_dict(orient="records")
    print(bod_data)

    check_month = bod_data[0]["month"] == month

except IndexError:
    print("Today NO BIRTHDAY")

else:
    if check_month:
        for x in bod_data:
            print(x["name"])
            # GET DATA FROM CSV FILE
            name = x["name"]
            email = x["email"]

            #   TEMPLATE UPDATE FOR SENDING
            template = ""
            temps = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
            # print(choice(temps))

            with open(f"letter_templates/{choice(temps)}", mode="r") as temp_file:
                read_data = temp_file.read()
                read_data = read_data.replace("[NAME]", name)
                print(read_data)
                template += read_data

            # SEND MAIL TO WISH BIRTHDAY
            my_email = "pythonemailtesting76@gmail.com"
            password = "9534857622"

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Happy BirthDay!\n\n{template}"
                )

