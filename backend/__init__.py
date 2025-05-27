from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World!</p>"

@app.route("/bye")
def bye_world():
    return "<div> goodbye world! </div>"

@app.route('/<name>')
def hi_kevin(name):
    return f'Hi {escape(name)}'
