from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models.dojo import Dojo



@app.route("/")
def index():
    list_of_dojos = Dojo.get_all()
    print(list_of_dojos)
    return render_template("dojos/index.html", dojos = list_of_dojos)


@app.route("/dojos/new")
def new_dojo():
    return render_template("dojos/new_dojo.html")


@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create(request.form)
    print(request.form)

    return redirect("/")


@app.route("/dojos/<int:dojo_id>")
def display_dojo(dojo_id):
    return render_template("dojos/dojo_show.html", dojo = Dojo.get_dojos_with_ninjas({"id": dojo_id}))



