from db import db
from sqlalchemy.sql import text


def get_project_members(project_id):
    sql = text(
        "SELECT user_id, user_name, user_role FROM project_members WHERE project_id=:project_id"
    )
    result = db.session.execute(sql, {"project_id": project_id})
    print(result)
    return result.fetchall()


def get_user_projects(user_id):
    sql = text(
        "SELECT projects.project_name FROM project_members, projects WHERE projects.id=project_members.project_id AND user_id=_user_id"
    )
    result = db.session.execute(sql, {"user_id": user_id})
    project_names = result.fetchall()
    return project_names


def add_user_project(id, name, role, project_id):
    project_id = int(project_id)
    sql = text(
        "INSERT INTO project_members (user_id, user_name, user_role, project_id) VALUES (:id, :name, :role, :project_id)"
    )
    db.session.execute(
        sql, {"id": id, "name": name, "role": role, "project_id": project_id}
    )
    db.session.commit()
    return
