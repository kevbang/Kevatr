from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World!</p>"

@app.route("/bye")
def bye_world():
    return "<div> goodbye world! </div>"