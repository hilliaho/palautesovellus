from db import db
from sqlalchemy.sql import text


def get_projects():
    result = db.session.execute(text("SELECT * FROM projects"))
    return result.fetchall()


def get_project(id):
    sql = f"SELECT * FROM projects WHERE id={id}"
    result = db.session.execute(text(sql))
    return result.fetchone()


def new_project(project_name):
    sql = f"INSERT INTO projects (project_name) VALUES ('{project_name}')"
    db.session.execute(text(sql))
    db.session.commit()
