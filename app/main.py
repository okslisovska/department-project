import requests
from flask import Blueprint, request, url_for, render_template, jsonify


bp = Blueprint('main', __name__)
ENDPOINTS = [('departments', 'GET'), ('employees', 'GET, POST'), ('employees/<id>', 'GET, PUT, DELETE')]


def resp_json(endpoint):
    """
    aggregate the full path to the specified api endpoint, send request, and return json data from response
    """
    api_url = request.host_url[:-1] + url_for(endpoint)
    resp = requests.get(api_url)
    return resp.json()


@bp.route('/')
@bp.route('/departments')
def departments():
    departments = resp_json('api.all_departments')
    employees = resp_json('api.all_employees')
    for department in departments:
        salaries = [emp['salary'] for emp in employees if emp['department'] == department['name']]
        department['salary_avg'] = sum(salaries) // len(salaries)
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
