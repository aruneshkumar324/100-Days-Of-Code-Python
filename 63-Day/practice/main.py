from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():

    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        all_books.append({
            "title": name,
            "author": author,
            "rating": rating
        })

    print(all_books)

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

