from db import db
from sqlalchemy.sql import text


def get_project_members(project_id):
    sql = text("SELECT * FROM project_members WHERE project_id=:project_id")
    result = db.session.execute(sql, {"project_id": project_id})
    return result.fetchall()


def get_project_member(project_id, user_id):
    sql = text(
        "SELECT * FROM project_members WHERE project_id=:project_id, user_id=:user_id"
    )
    result = db.session.execute(sql, {"project_id": project_id, "user_id": user_id})
    return result.fetchone()


def get_user_projects(user_id):
    sql = text("SELECT * FROM project_members WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    project_list = result.fetchall()
    projects = []
    for project in project_list:
        id = project.project_id
        sql = text("SELECT * FROM projects WHERE id=:id")
        result = db.session.execute(sql, {"id": id})
        projects.append(result.fetchone())
    return projects


def add_user_project(id, name, role, project_id):
    project_id = int(project_id)
    sql = text("INSERT INTO project_members VALUES (:id, :name, :role, :project_id)")
    db.session.execute(
        sql, {"id": id, "name": name, "role": role, "project_id": project_id}
    )
    db.session.commit()
    return
