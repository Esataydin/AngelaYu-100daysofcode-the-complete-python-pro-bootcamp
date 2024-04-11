from flask import render_template, redirect, url_for

from database import db, app, BlogPost
from forms import CreatePostForm


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.session.query(BlogPost).get(index)
    return render_template("post.html", post=requested_post)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=edit_form, is_edit=post_id)


@app.route("/new-post", methods=["POST", "GET"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_blog_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date="2023"
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route("/delete/<post_id>", methods=["GET", "DELETE"])
def delete_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
