from apps.home import blueprint
from flask import render_template, request, session
from flask_login import login_required
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename
from apps.authentication.models import Teams
from apps import db


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/teams')
@login_required
def teams():
    all_teams = Teams.query.filter_by(user_id=session["_user_id"])
    print(Teams.query.filter_by(user_id=session["_user_id"]))
    # print(session["_user_id"])
    # me=Teams(name='jke', color='red', user_id=session["_user_id"])
    # db.session.add(me)
    # db.session.commit()
    return render_template('home/teams.html', segment='teams', all_teams=all_teams)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
