from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")