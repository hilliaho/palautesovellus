from db import db
from sqlalchemy.sql import text


def get_project_members(project_id):
    sql = f"SELECT * FROM project_members WHERE project_id='{project_id}'"
    result = db.session.execute(text(sql))
    return result.fetchall()


def get_project_member(project_id, user_id):
    sql = f"SELECT * FROM project_members WHERE project_id='{project_id}' user_id='{user_id}'"
    result = db.session.execute(text(sql))
    return result.fetchone()


def get_user_projects(user_id):
    sql = f"SELECT * FROM project_members WHERE user_id='{user_id}'"
    result = db.session.execute(text(sql))
    project_list = result.fetchall()
    projects = []
    for project in project_list:
        id = project.project_id
        sql = f"SELECT * FROM projects WHERE id='{id}'"
        result = db.session.execute(text(sql))
        projects.append(result.fetchone())
    return projects


def add_user_project(user_id, user_name, user_role, project_id):
    sql = f"INSERT INTO project_members VALUES ({user_id},'{user_name}','{user_role}',{project_id})"
    db.session.execute(text(sql))
    db.session.commit()
    return
