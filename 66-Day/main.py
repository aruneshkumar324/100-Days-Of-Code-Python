from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from sqlalchemy_serializer import SerializerMixin


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify(cafes={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })
    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #
    #     # Put some properties in a sub-category
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # })


@app.route('/all')
def get_all_cafes():
    # ANGELA SOLUTION NOT WORKING
    # cafes = db.session.query(Cafe).all()
    # return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

    cafes = Cafe.query.all()

    cafeslist = []
    for cafe in cafes:
        cafeslist.append({
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
                "has_sockets": cafe.has_sockets,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "id": cafe.id,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "map_url": cafe.map_url,
                "name": cafe.name,
                "seats": cafe.seats

        })
    return jsonify(cafes=cafeslist)


@app.route('/search')
def search():
    location_url = request.args.get('loc')

    search_data = Cafe.query.filter_by(location=location_url).first()

    if search_data:
        # return jsonify(cafe={
        #     "can_take_calls": search_data.can_take_calls,
        #     "coffee_price": search_data.coffee_price,
        #     "has_sockets": search_data.has_sockets,
        #     "has_toilet": search_data.has_toilet,
        #     "has_wifi": search_data.has_wifi,
        #     "id": search_data.id,
        #     "img_url": search_data.img_url,
        #     "location": search_data.location,
        #     "map_url": search_data.map_url,
        #     "name": search_data.name,
        #     "seats": search_data.seats
        # })
        return jsonify(cafe=search_data.to_dict())
    else:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
