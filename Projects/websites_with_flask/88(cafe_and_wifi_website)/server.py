from flask import render_template, redirect, url_for, jsonify, request

import random

from forms import CafeForm
from database import app, db, Cafe


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    cafes = db.session.query(Cafe).all()
    list_of_rows = []
    list_of_rows.append(list(cafes[0].to_dict().keys()))
    # Makes a nested list of cafes, every element of "list_of_rows" is a list that contains cafe's information in order of "indexes".
    for cafe in cafes:
        list_of_rows.append(list(map(str, list(cafe.to_dict().values()))))
    indexes = ["Id", "Cafe Name", "Map URL", "Image URL", "Location", "Seats", "Has Toilet?", "Has Wifi?", "Has Sockets?", "Can Take Calls?", "Coffee Price"]
    # First element of list_of_rows is field names like "has_wifi", that's why we don't use it and add our indexes
    list_of_rows = list_of_rows[1:]
    return render_template('cafes.html', cafes=list_of_rows, indexes=indexes)


@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # Simply converts the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=bool(form.has_sockets.data),
            has_toilet=bool(form.has_toilet.data),
            has_wifi=bool(form.has_wifi.data),
            can_take_calls=bool(form.can_take_calls.data),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
        
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/delete', methods=["GET", "DELETE"])
def delete_cafe():
    cafe_id = request.args.get("cafe_id")
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("cafes"))


if __name__ == '__main__':
    app.run(debug=True)
