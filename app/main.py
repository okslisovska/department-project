import requests
from flask import Blueprint, request, url_for, render_template, jsonify


bp = Blueprint('main', __name__)

ENDPOINTS = [('departments', 'GET'),
             ('employees', 'GET, POST'),
             ('employees/<id>', 'GET, PUT, DELETE'),
             ('employees/search/<period>', 'GET')]


@bp.route('/')
@bp.route('/departments')
def departments():
    api_url_dep = request.host_url + url_for('api.all_departments')
    api_url_emp = request.host_url + url_for('api.all_employees')
    departments = requests.get(api_url_dep).json()
    employees = requests.get(api_url_emp).json()
    for department in departments:
        salaries = [emp['salary'] for emp in employees if emp['department'] == department['name']]
        department['salary_avg'] = sum(salaries) // len(salaries)
    return render_template('departments.html', departments=departments)


@bp.route('/departments/<string:name>')
def department(name):
    api_url = request.host_url + url_for('api.all_employees')
    resp = requests.get(api_url).json()
    employees = [employee for employee in resp if employee['department'] == name]
    return render_template('department.html', name=name, employees=employees)


@bp.route('/api')
def api():
    host_url = request.host_url
    return render_template('api.html', host_url=host_url, endpoints=ENDPOINTS)


@bp.route('/add', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        data = request.form
        api_url = request.host_url + url_for('api.create_employee')
        resp = requests.post(api_url, json=data).json()
        return render_template('add.html', message=resp["message"])
    return render_template('add.html', message="")


@bp.route('/search', methods=['GET', 'POST'])
def search_by_birthday():
    employees = []
    if request.method == 'POST':
        period = request.form['from'] + request.form['till']
        api_url = request.host_url + \
                  url_for('api.search_by_birthday', period=period)
        employees = requests.get(api_url).json()
    return render_template('search.html', employees=employees)
    







































