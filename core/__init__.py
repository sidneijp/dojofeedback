from flask import Flask
from views import views
from mongoengine import connect
import os

try:
    host=os.environ['MONGOHQ_URL']
except KeyError:
    host='localhost'

connect('app5623357', host=host)

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'dojofeedback'
app.register_blueprint(views)

if __name__ == "__main__":
    app.run()
