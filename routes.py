from app import app
from flask import render_template, request, redirect, session
import projects, users, feedback_messages, project_members, feedback_messages, input_validation


@app.route("/")
def index():
    list = projects.get_projects()
    name = users.get_session_username()
    return render_template("index.html", projects=list, username=name)


@app.route("/register", methods=["POST", "GET"])
def create_user():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_validation_result = input_validation.validate(
            "password", password, 8, 50
        )
        username_validation_result = input_validation.validate(
            "username", username, 2, 30
        )
        if username_validation_result != True:
            return render_template(
                "error_message.html", error_message=username_validation_result[1]
            )
        elif password_validation_result != True:
            return render_template(
                "error_message.html", error_message=password_validation_result[1]
            )
        elif users.create_user(username, password):
            return redirect("/")
        else:
            return render_template(
                "error_message.html",
                error_message="Käyttäjätunnus on jo käytössä.",
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
                "error_message.html", error_message="Väärä käyttäjätunnus tai salasana."
            )


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/newproject", methods=["POST"])
def new_project():
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error_message.html", error_message="Pääsy kielletty")
    project_name = request.form["project"]
    project_name_validation_result = input_validation.validate(
        "project_name", project_name, 1, 30
    )
    if project_name_validation_result != True:
        return render_template(
            "error_message.html", error_message=project_name_validation_result[1]
        )
    projects.new_project(project_name)
    return redirect("/")


@app.route("/my_feedback", methods=["GET"])
def my_feedback():
    list = feedback_messages.get_feedback_messages(users.get_id())
    return render_template("my_feedback.html", feedback_messages=list)


@app.route("/project/<int:project_id>", methods=["GET", "POST"])
def project(project_id):
    if request.method == "GET":
        list = project_members.get_project_members(project_id)
        project = projects.get_project_name(project_id)
        return render_template(
            "project_members.html",
            project_members=list,
            project=project,
            project_id=project_id,
        )
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template(
                "error_message.html", error_message="Pääsy kielletty"
            )
        receiver_id = request.form["receiver_id"]
        feedback_message_content = request.form["feedback_content"]
        message_validation_result = input_validation.validate(
            "message", feedback_message_content, 1, 5000
        )
        if message_validation_result != True:
            return render_template(
                "error_message.html", error_message=message_validation_result[1]
            )
        feedback_messages.send(feedback_message_content, receiver_id, project_id)
        address = f"/project/{project_id}"
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
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template(
                "error_message.html", error_message="Pääsy kielletty"
            )
        project_id = request.form["project_id"]
        user_name = request.form["user_name"]
        user_role = request.form["user_role"]
        name_validation_result = input_validation.validate("name", user_name, 1, 30)
        if name_validation_result != True:
            return render_template(
                "error_message.html", error_message=name_validation_result[1]
            )
        role_validation_result = input_validation.validate("role", user_role, 0, 30)
        if role_validation_result != True:
            return render_template(
                "error_message.html", error_message=role_validation_result[1]
            )
        user_id = users.get_id()
        if not project_members.is_user_in_project(user_id, project_id):
            project_members.add_user_project(
                id=user_id,
                name=user_name,
                role=user_role,
                project_id=project_id,
            )
        else:
            return render_template(
                "error_message.html",
                error_message="Et voi liittyä samaan projektiin kuin kerran.",
            )
        return redirect("my_projects")
