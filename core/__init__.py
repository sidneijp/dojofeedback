# encoding: utf-8

from flask import Flask, render_template
from views import views
from mongoengine import connect
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'dojofeedback'
app.register_blueprint(views)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error(e):
    return render_template('500.html'), 500

try:
    host = os.environ['MONGOHQ_URL']
    app.debug = False
except KeyError:
    host = 'localhost'
    app.debug = True

connect('app5623357', host=host)

if __name__ == "__main__":
    app.run()
