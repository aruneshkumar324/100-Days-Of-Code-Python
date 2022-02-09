from flask import Flask, render_template
import requests


app = Flask(__name__)

all_post = requests.get(url='https://api.npoint.io/4af156202f984d3464c3').json()
print(all_post)


@app.route('/')
def home():
    return render_template("index.html", posts=all_post)


@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for blog_post in all_post:
        if blog_post['id'] == post_id:
            requested_post = blog_post
    return render_template('post.html', post_id=post_id, r_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
