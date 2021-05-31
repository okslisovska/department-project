import requests
from flask import Blueprint, request, url_for, render_template, jsonify


bp = Blueprint('main', __name__)
ENDPOINTS = ['departments GET', 'employees GET, POST', 'employees/<id> GET, PUT, DELETE']


def resp_json(url_f):
    api_url = request.host_url[:-1] + url_for(url_f)
    resp = requests.get(api_url)
    return resp.json()


@bp.route('/')
@bp.route('/departments')
def departments():
    departments = resp_json('api.all_departments')
    return render_template('departments.html', departments=departments)


@bp.route('/departments/<string:name>')
def department(name):
    resp = resp_json('api.all_employees')
    employees = [employee for employee in resp if employee['department'] == name]
    return render_template('department.html', name=name, employees=employees)


@bp.route('/api')
def api():
    host_url = request.host_url
    return render_template('api.html', host_url=host_url, endpoints=ENDPOINTS)
