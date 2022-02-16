# import sqlite3
#
# db = sqlite3.connect('books.db')
#
# cursor = db.cursor()
#
# # cursor.execute('CREATE TABLE books '
# #                '(id INTEGER PRIMARY KEY, '
# #                'title varchar(250) NOT NULL UNIQUE, '
# #                'author varchar(250) NOT NULL, '
# #                'rating FLOAT NOT NULL)')
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# db.create_all()


# new_book = Books(title='Harry Potter', author='J. K. Rowling', rating=9.3)
# db.session.add(new_book)
# db.session.commit()


all_books = Books.query.all()
print(all_books)


book = Books.query.filter_by(title="Harry Potter").first()
print(book)


# book_update = Books.query.filter_by(title='Harry Potter').first()
# book_update.title = 'Harry Potter and the Goblet of Fire'
# db.session.commit()


# book_update = Books.query.get(1)
# book_update.title = '1 - Harry Potter and the Goblet of Fire'
# db.session.commit()


delete_book = Books.query.get(1)
db.session.delete(delete_book)
db.session.commit()













