from flask import Blueprint

views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')

@views.route('/')
def hello():
    return "Hello World!"