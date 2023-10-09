from db import db
from sqlalchemy.sql import text


def get_feedback_messages(receiver_id):
    sql = f"SELECT content FROM feedback_messages WHERE receiver_id={receiver_id} ORDER BY id"
    result = db.session.execute(text(sql))
    return result.fetchall()


def send(message, project_id, receiver_id):
    sql = f"INSERT INTO feedback_messages (content, project_id, receiver_id) VALUES ('{message}', {receiver_id}, {project_id})"
    db.session.execute(text(sql))
    db.session.commit()
    return True
