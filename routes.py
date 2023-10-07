from app import app
from flask import render_template, request, redirect
import groups, users


@app.route("/")
def index():
    list = groups.get_groups()
    return render_template("index.html", groups=list)


@app.route("/createuser", methods=["POST"])
def create_user():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.create_user(username, password):
            return redirect("/")
        else:
            return render_template(
                "error_message.html", message="Uuden käyttäjän luominen ei onnistunut."
            )


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template(
                "error_message.html", message="Kirjautuminen ei onnistunut."
            )


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/newgroup", methods=["POST"])
def new_group():
    group_name = request.form["group"]
    groups.new_group(group_name)
    return redirect("/")
