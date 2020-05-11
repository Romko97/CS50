from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first1():
    return render_template("first.html")

@app.route("/second")
def second1():
    return render_template("second.html")

@app.route("/third")
def third1():
    return render_template("third.html")