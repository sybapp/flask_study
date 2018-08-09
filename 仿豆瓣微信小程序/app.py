from flask import Flask, render_template
from context import *

context = {
    'movies': movies,
    'tvs': tvs,
}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', **context)


@app.route('/list/<id>')
def list(id):
    if id == '1':
        items = movies
    else:
        items = tvs
    return render_template('list.html', items=items)

