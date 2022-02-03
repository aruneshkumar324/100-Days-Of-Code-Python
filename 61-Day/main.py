from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


app = Flask(__name__)

app.secret_key = 'helloarunesh'


class Login(FlaskForm):
    email = StringField(label='Email : ')
    password = PasswordField(label='Password : ')
    submit = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
