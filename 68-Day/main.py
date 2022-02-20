from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'helloaruneshhowareyou'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # def is_active(self):
    #     """True, as all users are active."""
    #     return True
    #
    # def get_id(self):
    #     """Return the email address to satisfy Flask-Login's requirements."""
    #     return self.email
    #
    # def is_authenticated(self):
    #     """Return True if the user is authenticated."""
    #     return self.authenticated
    #
    # def is_anonymous(self):
    #     """False, as anonymous users aren't supported."""
    #     return False

# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hash_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)

        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=hash_password,
        )

        db.session.add(new_user)
        db.session.commit()

        return render_template('secrets.html', user=new_user.name)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    filename = 'cheat_sheet.pdf'
    return send_from_directory(
        directory="static/files",
        path=filename,
        as_attachment=False
    )


@app.route('/delete', methods=['GET', 'POST'])
def delete_users():
    users = User.query.all()
    for user in users:
        user_id = user.id
        db.session.delete(user)
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
