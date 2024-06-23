from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '플라스크 실습'

app.run(debug = True)