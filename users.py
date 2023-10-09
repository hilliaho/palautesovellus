from db import db
from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    sql = f"SELECT id, username, password FROM users WHERE username='{username}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return True
        else:
            return False


def logout():
    del session["user_id"]


def create_user(username, password):
    try:
        hash_value = generate_password_hash(password)
        sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{hash_value}')"
        db.session.execute(text(sql))
        db.session.commit()
    except:
        return False
    return login(username, password)


def get_id():
    return session.get("user_id", 0)


def get_session_username():
    return session.get("username", None)


def get_user(id):
    sql = f"SELECT * FROM users WHERE id={id}"
    result = db.session.execute(text(sql))
    return result.fetchone()
