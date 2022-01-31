from flask import Flask
from random import randint


num = randint(0, 9)
print(num)

app = Flask(__name__)


@app.route('/')
def home():

    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o8doKOr3E5hvVT8Sk/giphy.gif'/>"


@app.route('/<int:number>')
def guess(number):
    if number == num:
        return "<h1>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif number > num:
        return "<h1>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number < num:
        return "<h1>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
