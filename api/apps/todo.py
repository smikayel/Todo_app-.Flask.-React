from flask import Blueprint, request, json, jsonify
from apps.models import Todo, db

todoApi = Blueprint('todoApi', __name__)


@todoApi.route('/', methods=["GET"])
def todo():
    todo_list = Todo.query.all()
    return [{"id": todo_el.id, "title": todo_el.title, "complete": todo_el.complete} for todo_el in todo_list], 200


@todoApi.route("/", methods=["POST"])
def add_todo():
    try:
        body = json.loads(request.data)
        title = body["title"]
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()

        return new_todo.serialize(), 201

    except Exception as error:
        return error, 500


@todoApi.route("/delete/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        if not todo:
            return {"message": f"Todo with id:{todo_id} not found!"}, 401
        db.session.delete(todo)
        db.session.commit()
        return todo.serialize(), 200
    except Exception as error:
        return error, 500


@todoApi.route("/update/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        db.session.commit()
        return todo.serialize(), 200
    except Exception as error:
        return error, 500
