from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_gravatar import Gravatar

from functools import wraps
from datetime import date

from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from database import db, app, User, BlogPost, Comment


gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    if current_user.is_authenticated:
        id = current_user.id
        if id == 1:
            is_admin = True
        else:
            is_admin = False
    else:
        is_admin = False
    return render_template("index.html", all_posts=posts, is_admin=is_admin)


# ------------------------------------------------- USER -------------------------------------------------#
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        # Email doesn't exist
        if not user:
            error = "That email does not exist, please try again."
        # Password incorrect
        elif not check_password_hash(user.password, password):
            error = 'Password incorrect, please try again.'
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, error=error)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # If user's email already exists
        if User.query.filter_by(email=form.email.data).first():
            # Sends flash message
            flash("You've already signed up with that email, log in instead!")
            # Redirects to /login route.
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

# Creates admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.is_authenticated:
            if current_user.id != 1:
                return abort(403)
        else:
            return abort(403)
        # Otherwise continues with the route function
        return f(*args, **kwargs)
    return decorated_function

# ------------------------------------------------- POST ------------------------------------------------- #
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html", post=requested_post, form=form, current_user=current_user)


@app.route("/new-post", methods=["POST", "GET"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["PATCH", "GET"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
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
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>", methods=["GET", "DELETE"])
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
