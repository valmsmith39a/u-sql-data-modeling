from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://georgewee@localhost:5432/example'

db = SQLAlchemy(app)

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
