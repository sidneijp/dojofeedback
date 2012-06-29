from flask import Flask
from views import views
from mongoengine import connect


connect('dojofeedback',
    host='localhost',
    port=27017,
    username='',
    password='')

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'dojofeedback'
app.register_blueprint(views)

if __name__ == "__main__":
    app.run()
