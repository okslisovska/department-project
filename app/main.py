import requests
from flask import Blueprint, request, url_for, render_template


bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/departments')
def departments():
    api_url = request.host_url[:-1] + url_for('api.get_departments')
    response = requests.get(api_url)
    departments = response.json()
    return render_template('index.html', departments=departments)


ENDPOINTS = ['departments', 'employees/<id>']

@bp.route('/api')
def api():
    host_url = request.host_url
    return render_template('api.html', host_url=host_url, endpoints=ENDPOINTS)

