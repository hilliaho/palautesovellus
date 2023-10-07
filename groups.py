from db import db
from sqlalchemy.sql import text


def get_groups():
    result = db.session.execute(text("SELECT content FROM groups"))
    return result.fetchall()


def new_group(group_name):
    sql = f"INSERT INTO groups (content) VALUES ('{group_name}')"
    db.session.execute(text(sql))
    db.session.commit()
