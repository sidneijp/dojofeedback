from flask import Flask
from views import views
from mongoengine import connect


connect('app5623357',
    host='flame.mongohq.com',
    port=27089,
    username='dojofeedback',
    password='android2k11')

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'dojofeedback'
app.register_blueprint(views)

if __name__ == "__main__":
    app.run()
