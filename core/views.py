# encoding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for, Response, flash
from models import Dojo, Comment
from forms import DojoForm
from services import create_qrcode
import simplejson
import random

views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')


@views.route('/')
def index():
    form = DojoForm()
    return render_template('dojo.html', form=form)


@views.route('/dojo/<name>/')
def comment(name):
    dojo = Dojo.get_or_404(name=name)
    return render_template('comentarios.html', dojo=dojo)


@views.route('/dojo/<name>/feedback/')
def feedback(name):
    dojo = Dojo.get_or_404(name=name)
    return render_template('feedback.html', dojo=dojo)


@views.route('/dojo/create/', methods=['POST'])
def create():
    response = {'success': False}
    form = DojoForm(request.form)
    if form.validate():
        dojo = Dojo(name=request.form['name'])
        host = request.headers['Origin']

        dojo.save()

        response['dojo_link'] = host + url_for('.comment', name=dojo.name)
        response['feedback_link'] = host + url_for('.feedback', name=dojo.name)

        create_qrcode(response['dojo_link'])

        response['success'] = True
    else:
        response['errors'] = []
        for error in form.name.errors:
            response['errors'].append(error)
    return Response(simplejson.dumps(response), mimetype="application/json")


@views.route('/feedback/create/', methods=['POST'])
def create_feedback():
    dojo = Dojo.get_or_404(id=request.form['dojo_id'])
    comment = request.form['comment'].strip()

    if comment:
        comment = Comment(description=comment,
            status=request.form['status'])
        dojo.comments.append(comment)
        random.shuffle(dojo.comments)
        dojo.save()
        flash('Comentario salvo com sucesso', 'success')

    else:
        flash('Comentario em branco', 'error')
    return redirect('/dojo/%s' % dojo.name)
