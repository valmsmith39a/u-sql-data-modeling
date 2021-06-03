from flask import Flask

# instantiate application 
# create an instance of Flask 
app = Flask(__name__)

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

@app.route('/')
def index(): 
  return 'Hello Cheeze!'

