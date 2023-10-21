from db import db
from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import secrets


def login(username, password):
    sql = text("SELECT id, username, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False


def logout():
    del session["user_id"]


def create_user(username, password):
    try:
        hash_value = generate_password_hash(password)
        sql = text(
            "INSERT INTO users (username, password) VALUES (:username, :password)"
        )
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)


def get_id():
    return session.get("user_id", 0)


def get_session_username():
    return session.get("username", None)


def get_user(id):
    sql = text("SELECT * FROM users WHERE id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()
