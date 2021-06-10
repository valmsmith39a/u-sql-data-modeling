from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

import sys 
import os 

app = Flask(__name__)  # create an application named after our file (app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_URI")

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
	__tablename__ = "todos"
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)
	completed = db.Column(db.Boolean, nullable=False, default=False)
	def __repr__(self):
			return f"<Todo {self.id} {self.description}>"

class TodoList(db.Model):
	__tablename__ = 'todolists'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	todos = db.relationship('Todo', backref='list', lazy=True)


#db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  error = False
  body = {}
  try:
    description = request.json['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if not error:
      return jsonify(body)

@app.route("/")
def index():
    print('inside root')
    return render_template("index.html", data=Todo.query.all())


