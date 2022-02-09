from flask import Flask, render_template
import requests


app = Flask(__name__)
all_posts = requests.get(url='https://api.npoint.io/24c6b2680163e0c6bf8b').json()


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post_page(post_id):
    requested_post = None
    for post in all_posts:
        if post['id'] == post_id:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
