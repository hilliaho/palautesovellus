from db import db
from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    sql = f"SELECT id, password FROM users WHERE username='{username}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = username
            return True
        else:
            return False


def logout():
    del session["username"]


def create_user(username, password):
    try:
        hash_value = generate_password_hash(password)
        sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{hash_value}')"
        db.session.execute(text(sql))
        db.session.commit()
    except:
        return False
    return login(username, password)