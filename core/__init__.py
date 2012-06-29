from flask import Flask
from views import views

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'dojofeedback'
app.register_blueprint(views)

if __name__ == "__main__":
    app.run()
