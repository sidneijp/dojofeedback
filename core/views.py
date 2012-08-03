from flask import Blueprint, render_template, request, redirect, jsonify
from models import Dojo, Comment
from forms import DojoForm

views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')


@views.route('/')
def index():
    form = DojoForm()
    return render_template('dojo.html', form=form)


@views.route('/dojo/<name>')
def show(name):
    dojo = Dojo.get_or_404(name=name)

    return render_template('comentarios.html', dojo=dojo)


@views.route('/dojo/<dojo_name>/feedback')
def feedback(dojo_name):
    dojo = Dojo.get_or_404(name=dojo_name)

    return render_template('feedback.html', dojo=dojo)


@views.route('/dojo/create', methods=['POST'])
def create():
    form = DojoForm(request.form)
    if form.validate():
        dojo = Dojo(name=request.form['name'])
        dojo.save()
        return redirect('/dojo/%s' % dojo.name)
    return render_template('dojo.html', form=form)

@views.route('/feedback/create', methods=['POST'])
def create_feedback():
    dojo = Dojo.get_or_404(id=request.form['dojo_id'])
    comment = Comment(description=request.form['comment'],
        status=request.form['status'])
    dojo.comments.append(comment)
    dojo.save()

    return redirect('/dojo/%s' % dojo.name)
