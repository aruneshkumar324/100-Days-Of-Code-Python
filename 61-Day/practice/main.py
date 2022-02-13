from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm


app = Flask(__name__)
app.secret_key = 'hello arunesh how are you'


class LoginForm(FlaskForm):
    username = StringField(label='Username')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
