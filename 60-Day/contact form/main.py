from flask import Flask, render_template, request
import requests
from componets import mail_send

app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/9d474babfbdf3a487bf2").json()


@app.route("/")
def home():
    return render_template('index.html', posts=response)


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in response:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)

        mail_send(name, email, phone, message)

        return render_template('contact.html', is_sent=True)
    return render_template('contact.html', is_sent=False)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
