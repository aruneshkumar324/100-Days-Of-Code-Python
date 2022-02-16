from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# db.create_all()


@app.route('/')
def home():
    return render_template('index.html', library=Book.query.all())


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        new_book = Book(title=name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_update = Book.query.get(book_id)
        book_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book = Book.query.get(book_id)
    return render_template('edit.html', book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

