# import smtplib
#
# my_email = "pythonemailtesting76@gmail.com"
# password = "9534857622"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pythonemailtesting76@yahoo.com",
#         msg='Subject:Hello 2\n\nThis is body message 2'
#     )
#
#
# # connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(.
# #         from_addr=my_email,
# #         to_addrs="pythonemailtesting76@yahoo.com",
# #         msg='Subject:Hello 2\n\nThis is body message 2'
# #     )
# # connection.close()


import datetime as dt


now = dt.datetime.now()

print(now)
print(type(now))


print(now.year)
print(type(now.year))

print(now.month)
print(now.weekday())


DOB = dt.datetime(year=1999, month=7, day=15, hour=9, minute=36, second=24)
print(DOB)
























