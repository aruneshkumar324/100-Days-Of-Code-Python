from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Home</h1>" \
           "<p>Paragraph</p>" \
           "<img src='https://media.giphy.com/media/26FLdmIp6wJr91JAI/giphy.gif' />"


def make_bold(fun):
    def wrapper():
        return f'<b>{fun()}</b>'
    return wrapper

def make_emphasis(fun):
    def wrapper():
        return f"<em>{fun()}</em>"
    return wrapper

def make_underline(fun):
    def wrapper():
        return f"<u>{fun()}</u>"
    return wrapper

@app.route('/blog')
@make_bold
@make_emphasis
@make_underline
def blog():
    return "BLOG"


@app.route('/username/<name>/<int:num>')
def about(name, num):
    return f"Hello {name}, total {10 - num}"


# AUTHENTICATION CHECK

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False





@app.route('/profile')
def profile():
    return "<h1>Welcome</h1>"





























if __name__ == "__main__":
    app.run(debug=True)
