from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task


@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))
        return render_template("create.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form["description"]
        task.completed = "completed" in request.form
        db.session.commit()
        return redirect(url_for("index"))
        return render_template("edit.html", task=task)


@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))
