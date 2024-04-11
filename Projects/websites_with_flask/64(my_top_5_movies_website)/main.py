from flask import render_template, redirect, url_for, request

import requests

from database import db, app, Movie
from forms import RateMovieForm, FindMovieForm


MOVIE_DB_API_KEY = YOUR_MOVIE_DB_API_KEY


@app.route("/")
def home():
    movies_list = Movie.query.order_by(Movie.rating).all()
    # This line loops through all the movies
    for i in range(len(movies_list)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        movies_list[i].ranking = len(movies_list) - i
    db.session.commit()
    return render_template("index.html", movies_list=movies_list)


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
    MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["original_title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
