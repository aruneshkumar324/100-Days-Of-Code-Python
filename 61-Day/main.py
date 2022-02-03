from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

# i have insllated -> email_validator


app = Flask(__name__)

app.secret_key = 'helloarunesh'


class Login(FlaskForm):
    email = EmailField(label='Email : ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password : ', validators=[DataRequired(), Length(min=8, message='Field must be at least 8 characters long.')])
    submit = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
