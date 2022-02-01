from flask import Flask, render_template
from random import randint
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    random_num = randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', num=random_num, current_year=year)


if __name__ == "__main__":
    app.run(debug=True)
