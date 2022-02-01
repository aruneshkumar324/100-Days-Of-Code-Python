from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<id>')
def post(id):
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)
