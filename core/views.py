from flask import Blueprint, render_template, request, redirect, url_for
from models import Dojo, Comment
from forms import DojoForm
import simplejson

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
    response = {}
    form = DojoForm(request.form)
    if form.validate():
        dojo = Dojo(name=request.form['name'])
        dojo.save()
        response['feedback_link'] = url_for('.feedback', dojo_name=dojo.name)
        return response

    return simplejson.dumps(response)


@views.route('/feedback/create', methods=['POST'])
def create_feedback():
    dojo = Dojo.get_or_404(id=request.form['dojo_id'])
    comment = Comment(description=request.form['comment'],
        status=request.form['status'])
    dojo.comments.append(comment)
    dojo.save()

    return redirect('/dojo/%s' % dojo.name)
