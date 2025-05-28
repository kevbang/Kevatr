from flask import Flask
from flask import url_for
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

# URL Building
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('hi_kevin', name='jill'))
