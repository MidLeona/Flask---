from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def welcome():
  return 'Welcome'

@app.route('/create/')
def create():
  return 'Create new page'

@app.route('/read/<id>/')
def read(id):
  return 'Read ' + id + ' page'

app.run(debug = True)  