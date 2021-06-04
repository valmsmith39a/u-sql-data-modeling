from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate application 
# create an instance of Flask 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://georgewee@localhost:5432/example'

"""
 all configuration variables in a Flask application set on dictionary app.config 
 Flask SQL Alchemy expects a configuration variable called SQLALCHEMY_DATABASE_URI
 SQLALCHEMY_DATABSE_URI: tells SQLAlchemy how to connect to the database

db = SQLAlchemy(app)

postgresql: dialect (ex postgresql, sqlite, mysql) SQLAlchemy can be used with different database systems 
  can add the database api (database adapter) as an option
  ex. 
    postgresql+psycopg2://myusername... 

username: name of user to login on the host machine 

host: IP address - localhost == 127.0.0.1

5432: port: connection port used on host 

mydatabase: name of your database

"""
"""
  Created a hello cheeze application 
  Configured a connection from SQLAlchemy to Flask application 
  Create a record within a table, read from that table have hello cheeze application print name from our database 

  db = SQLAlchemy(app): db is an instance of your database. comes from SQLAlchemy class imported from the flask_sqlalchemy library. db provides an interface to use SQLAlchemy. 

    db provides several objects 
      db.Model: objecct that gives ability to create and manipulate models (classes, map to tables within or database). models are classes are tables  
      db.sesson: ability to create an manipulate transactions in the context of a session 

"""

"""
 @app: python decorator 
 @app.route('/'): tell flask application which endpoint (route) to listen to. listen to the "home page" route (root route) "/"
 def index(): is the route handler. listens to connections to the root route a
 @app.route: define a route
 def index: define a route handler 
 To run: 
 FLASK_APP=flask-hello-app.py: specify the location of our flask app 
 FLASK_APP=flask-hello-app.py flask run 
"""

"""
  Person class inherits from db.Model which links and connects to SQLAlchemy's mappings between classes and tables 

  id: primary key column 
  name: attribute with type and not null constraint 
  default: pick name of table for you - lowercase name of class 
  to set name of database: 
    __tablename__ = 'persons'

  create tables
    db.create_all(): detects models and creates tables (if they don't exist) 
    
"""
class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  
db.create_all()

@app.route('/')
def index(): 
  return 'Hello Cheeze!'

if __name__ == '__main__':
  app.run()
