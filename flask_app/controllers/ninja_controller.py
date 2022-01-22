from flask import render_template, redirect, request, session, url_for

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas/new")
def new_collar_page():
    return render_template("ninjas/new_ninja.html", dojos = Dojo.get_all())


@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)
    print(request.form)
    return redirect(url_for("display_dojo", dojo_id=request.form["dojo_id"]))
