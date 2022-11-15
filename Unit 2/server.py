from flask import Flask, render_template, redirect, url_for
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, Cupcake, Mini, read_csv, write_new_csv, add_cupcake
import csv


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/individual_cupcakes")
def individual_cupcakes():
    return render_template("individual_cupcakes.html")

@app.route("/all_cupcakes")
def all_cupcakes():
    return render_template("all_cupcakes.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/add_cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    if cupcake:
        add_cupcake_dictionary("currentorders.csv", cupcake)
        return redirect(url_for("all_cupcakes"))
    else:
        return "Sorry cupcake not found."

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")

