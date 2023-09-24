from sqlalchemy.sql import text
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT content FROM groups"))
    groups = result.fetchall()
    return render_template("index.html", groups=groups)

@app.route("/createuser", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{hash_value}')"
    db.session.execute(text(sql))
    db.session.commit()
    session["username"] = username
    return redirect("/")


@app.route("/login",methods=["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = f"SELECT id, password FROM users WHERE username='{username}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()
    print(user)    
    if not user:
        return redirect("/")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/")
        else:
            return redirect("/")
        

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/newgroup", methods=["POST"])
def new_group():
    content=request.form["group"]
    sql=f"INSERT INTO groups (content) VALUES ('{content}')"
    db.session.execute(text(sql))
    db.session.commit()
    return redirect("/")

