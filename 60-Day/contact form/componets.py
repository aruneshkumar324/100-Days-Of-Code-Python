from smtplib import SMTP


MY_EMAIL = 'pythonemailtesting76@gmail.com'
PASSWORD = '9534857622'
RECEIVER = 'pythonemailtesting76@yahoo.com'


def mail_send(name, email, phone, message):
    with SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER,
            msg=f"Subject:Contact Form\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )
