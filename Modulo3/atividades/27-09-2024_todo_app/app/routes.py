from flask import render_template, request, redirect, url_for, jsonify
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


# Rota para listar todas as tarefas em formato JSON
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task_to_json(task) for task in tasks])


# Rota para obter uma tarefa específica pelo ID
@app.route("/api/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task_to_json(task))


# Rota para criar uma nova tarefa via JSON
@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(task_to_json(new_task)), 201


# Rota para atualizar uma tarefa existente via JSON
@app.route("/api/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)
    db.session.commit()
    return jsonify(task_to_json(task))


# Rota para deletar uma tarefa
@app.route("/api/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 204


# Função auxiliar para converter Task em JSON
def task_to_json(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "created_at": task.created_at.isoformat(),
        "completed": task.completed,
    }
