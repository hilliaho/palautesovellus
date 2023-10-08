from app import app
from flask import render_template, request, redirect
import projects, users, feedback_messages, project_members, user_projects


@app.route("/")
def index():
    list = projects.get_projects()
    name = users.get_username()
    return render_template("index.html", projects=list, username=name)


@app.route("/createuser", methods=["POST"])
def create_user():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.create_user(username, password):
            return redirect("/")
        else:
            return render_template(
                "error_message.html", message="Uuden käyttäjän luominen ei onnistunut."
            )


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template(
                "error_message.html", message="Kirjautuminen ei onnistunut."
            )


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/newproject", methods=["POST"])
def new_project():
    project_name = request.form["project"]
    projects.new_project(project_name)
    return redirect("/")


@app.route("/my_feedback", methods=["GET"])
def my_feedback():
    list = feedback_messages.get_feedback_messages(users.get_id)
    return render_template("my_feedback.html", feedback_messages=list)


@app.route("/project/<int:id>", methods=["GET", "POST"])
def project(id):
    if request.method == "GET":
        list = project_members.get_project_members(id)
        project = projects.get_project(id)
        return render_template(
            "project_members.html", project_members=list, project=project
        )
    if request.method == "POST":
        user_id = users.get_id()
        name = request.form["name"]
        project_members.add_project_member(user_id, id, name)
        address = f"/project/{id}"
        return redirect(address)


@app.route("/my_projects", methods=["GET", "POST"])
def user_projects():
    if request.method == "GET":
        user_id = users.get_id()
        all_projects = projects.get_projects()
        user_projects = project_members.get_user_projects(user_id)
        return render_template(
            "user_projects.html", user_projects=user_projects, all_projects=all_projects
        )
    if request.method == "POST":
        project_id = request.form["project_id"]
        user_name = request.form["user_name"]
        user_role = request.form["user_role"]
        user_id = users.get_id()
        project_members.add_user_project(
            user_id=user_id,
            user_name=user_name,
            user_role=user_role,
            project_id=project_id,
        )
        return redirect("my_projects")
