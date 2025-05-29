from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape

# flask --app __init__.py run

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

@app.route("/login", methods=["GET", "POST"])
def login():
    payload = "wapapapalala"
    if request.method == 'POST':
        return f'Hi {payload}'
    else:
        return f"SOOOOPAALALALA"


# URL Building
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('hi_kevin', name='jill'))

# Static Files

url_for("static", filename="style.css")
