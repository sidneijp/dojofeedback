from flask import Blueprint, render_template, request
from models import Dojo

views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')


@views.route('/')
def index():
    return render_template('dojo.html')

@views.route('/dojo/create', methods=['POST'])
def create():
    dojo = Dojo(name=request.form['name'])
    dojo.save()
    return render_template('dojo.html', name=dojo.name) 
