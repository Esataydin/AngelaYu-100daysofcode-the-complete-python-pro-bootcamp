from twilio.rest import Client

from flask import Flask, render_template, request
import requests


app = Flask(__name__)

account_sid = YOUR_TWILIO_ACCOUNT_SID
auth_token = YOUR_TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = YOUR_TWILIO_VIRTUAL_NUMBER
YOUR_NUMBER = YOUR_TWILIO_NUMBER

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_num>")
def show_post(post_num):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == post_num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html", header="Contact Me")


@app.route("/contact", methods=["POST"])
def receive_data():
    """Gets the given data in contact route and sends a sms to [YOUR_NUMBER] with Twilio API """
    username = request.form['username']
    email = request.form['email']
    phone_number = request.form['phone-number']
    message = request.form['message']

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"Name: {username}\nE-mail: {email}\nPhone-number: {phone_number}\nMessage: {message}",
            from_=TWILIO_VIRTUAL_NUMBER,
            to=YOUR_NUMBER
        )
    print(message.sid)

    return render_template("contact.html", header="Your message successfully sent.")


if __name__ == "__main__":
    app.run(debug=True)
