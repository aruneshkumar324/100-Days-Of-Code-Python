from flask import Flask, render_template, request
import requests
from smtplib import SMTP


app = Flask(__name__)
all_posts = requests.get(url='https://api.npoint.io/24c6b2680163e0c6bf8b').json()
MY_EMAIL = 'pythonemailtesting76@gmail.com'
PASSWORD = '9534857622'


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)

        with SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='pythonemailtesting76@yahoo.com', msg=f'Subject:Contact Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}')

        return render_template('contact.html', mess='Successfully sent message')
    return render_template('contact.html', mess='Contact Me')


@app.route('/post/<int:post_id>')
def post_page(post_id):
    requested_post = None
    for post in all_posts:
        if post['id'] == post_id:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
