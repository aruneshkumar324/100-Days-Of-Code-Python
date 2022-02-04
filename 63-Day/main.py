from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_library.db'
# # Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(250), unique=True, nullable=False)
    author_book = db.Column(db.String(250), nullable=False)
    rating_book = db.Column(db.Float, nullable=False)


# db.create_all()


@app.route('/')
def home():
    #    MY SOLUTION FROM DOCUMENTATION
    # all_books = Book.query.all()

    # ANGELA SOLUTION
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        db.session.add(Book(book_name=title, author_book=author, rating_book=rating))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating_book = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    request_book = Book.query.get(book_id)
    return render_template('edit_rating.html', book=request_book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    db.session.delete(Book.query.get(book_id))
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

