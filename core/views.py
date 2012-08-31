from flask import Blueprint, render_template, request, redirect, url_for, Response
from models import Dojo, Comment
from forms import DojoForm
import simplejson
import httplib2

views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')
client = httplib2.Http()


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
    miud_url = 'http://miud.in/api-create.php?url={0}'
    response = {'success': False}
    form = DojoForm(request.form)
    if form.validate():
        dojo = Dojo(name=request.form['name'])
        host = request.headers['Origin']
        dojo.save()

        dojo_link = host + url_for('.comment', name=dojo.name)
        response['feedback_link'] = host + url_for('.feedback', name=dojo.name)

        miud_response = client.request(miud_url.format(dojo_link))

        dojo_link = miud_response[1]
        response['success'] = True
        response['dojo_link'] = dojo_link
    else:
        response['errors'] = []
        for error in form.name.errors:
            response['errors'].append(error)
    return Response(simplejson.dumps(response), mimetype="application/json")


@views.route('/feedback/create/', methods=['POST'])
def create_feedback():
    dojo = Dojo.get_or_404(id=request.form['dojo_id'])
    comment = Comment(description=request.form['comment'],
        status=request.form['status'])
    dojo.comments.append(comment)
    dojo.save()

    return redirect('/dojo/%s' % dojo.name)
