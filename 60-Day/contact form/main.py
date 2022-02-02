from flask import Flask, render_template
import requests


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


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
