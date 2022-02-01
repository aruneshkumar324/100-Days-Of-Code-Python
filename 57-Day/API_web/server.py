from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/guess/<username>')
def guess(username):
    # NAME & AGE FINDER
    response = requests.get(url=f"https://api.agify.io/?name={username}")
    data = response.json()
    age = data['age']

    # GENDER FINDER
    second_response = requests.get(url=f"https://api.genderize.io/?name={username}")
    gender = second_response.json()['gender']

    return render_template('index.html', name=username, user_age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
