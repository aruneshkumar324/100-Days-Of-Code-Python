from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collections.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)


class UpdateForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


# db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
#
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    return render_template("index.html", movies=Movie.query.all())


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = UpdateForm()
    movie_id = request.args.get('id')
    if request.method == 'POST':
        movie_update = Movie.query.get(movie_id)
        movie_update.rating = request.form['rating']
        movie_update.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
