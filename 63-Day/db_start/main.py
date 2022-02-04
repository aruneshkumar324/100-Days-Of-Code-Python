# import sqlite3
#
#
# db = sqlite3.connect('books-collection.db')
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE RECORD
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


# db.session.add(Book(title='Superb Book', author="Mohan Das", rating=8.3))
# db.session.commit()


# READ ALL BOOK
library = db.session.query(Book).all()


# READ SINGLE BOOK
read_book = Book.query.filter_by(title='Superb Book').first()
# print(read_book.title)


# UPDATE RECORD
update_book = Book.query.filter_by(title="Superb Book").first()
# update_book.title = 'Superb'
# db.session.commit()


# UPDATE RECORD BY PRIMARY KEY
update_book_by_id = Book.query.get(3)
# update_book_by_id.title = 'Super Book'
# db.session.commit()


# DELETE RECORD
delete_book = Book.query.get(2)
db.session.delete(delete_book)
db.session.commit()


































