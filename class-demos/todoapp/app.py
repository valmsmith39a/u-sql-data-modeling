from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # create an application named after our file (app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://georgewee@localhost:5432/todoapp"

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id} {self.description}>"


db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  print('inside create todos', request.get_json())
  description = request.json['description']
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return jsonify({
    'description': todo.description
  }) 


@app.route("/")
def index():
    print('inside root')
    return render_template("index.html", data=Todo.query.all())


