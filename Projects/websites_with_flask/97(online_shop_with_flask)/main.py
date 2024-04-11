from flask import render_template, flash, redirect, url_for
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

from forms import RegisterForm, LoginForm, ItemForm
from database import app, User, Cart, Item, db


# Additional information on https://docs.stripe.com/api?lang=python
stripe.api_key = YOUR_STRIPE_API_KEY


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id) -> User:
    return User.query.get(int(user_id))


@app.route('/')
def home():
    items = Item.query.all()
    return render_template('index.html', items=items)


@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    """Adds item to the database with given inputs."""
    form = ItemForm()
    if form.validate_on_submit():
        new_stripe_item = stripe.Price.create(
            currency='usd',
            unit_amount=int(f'{form.price.data}00'),
            product_data={'name': form.product_name.data}
        )
        new_item = Item(
            product_name=form.product_name.data,
            product_id=new_stripe_item.product,
            product_img_url=form.product_img_url.data,
            price=form.price.data,
            price_id=new_stripe_item.id
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('new-item.html', form=form)


# --------------------------------------------- CART ---------------------------------------------#
@app.route('/cart', methods=['GET', 'DELETE'])
def cart():
    items = Cart.query.filter_by(owner_id=current_user.id).all()
    return render_template('cart.html', items=items)


@app.route('/add/<int:item_id>', methods=['GET', 'POST'])
@login_required
def add_item_to_cart(item_id):
    item = Item.query.get(item_id)
    new_cart_item = Cart(
        cart_owner=current_user,
        item_id=item.id,
        product_name=item.product_name,
        product_id=item.product_id,
        product_img_url=item.product_img_url,
        price=item.price,
        price_id=item.price_id
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<int:cart_id>', methods=['GET', 'DELETE'])
@login_required
def delete_item_from_cart(cart_id):
    item_to_delete = Cart.query.get(cart_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('cart'))


# --------------------------------------------- USER --------------------------------------------- #
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
            # return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            error = 'Password incorrect, please try again.'
            # return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form, error=error)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # If user's email already exists
        if User.query.filter_by(email=form.email.data).first():
            # Send flash messsage
            flash("You've already signed up with that email, log in instead!")
            # Redirect to /login route.
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
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# --------------------------------------------- CHECKOUT-PAYMENT --------------------------------------------- #
YOUR_DOMAIN = 'http://127.0.0.1:5000'
@app.route('/create-checkout-session', methods=['GET' ,'POST'])
def create_checkout_session():
    """Creates a checkout session to payment for the items in cart"""
    try:
        line_items = []
        cart_items = Cart.query.filter_by(owner_id=current_user.id).all()
        for item in cart_items:
            price_dict = {
                'price': item.price_id,
                'quantity': 1
            }
            line_items.append(price_dict)
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/cancel')
def cancel():
    return render_template('cancel.html')


if __name__ == '__main__':
    app.run(debug=True)
