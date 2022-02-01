from flask import Flask, render_template
import requests


response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<id>')
def post(id):
    id = int(id)
    return render_template('post.html', posts=all_posts, post_id=id)


if __name__ == "__main__":
    app.run(debug=True)
