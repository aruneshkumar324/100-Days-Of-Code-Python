from flask import Flask, render_template, redirect
from wtforms import StringField, PasswordField, SubmitField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = 'hello arunesh how are you'
Bootstrap(app)


class LoginForm(FlaskForm):
    username = EmailField(label='Username', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.username.data)
        print(login_form.password.data)
        if login_form.username.data == "admin@email.com" and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
