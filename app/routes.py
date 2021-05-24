import requests
from flask import jsonify, url_for
from app import app
from app.models import Department, Employee


@app.route('/')
def index():
    return "<h1>Department-project</h1><p>will be here very soon</p>"

@app.route('/departments')
def departments():
    response = requests.get("http://localhost:5000/api/departments")
    return response.text

@app.route('/api/employees/<int:id>')
def get_employee(id):
    return jsonify(Employee.query.get_or_404(id).to_dict())

@app.route('/api/departments')
def get_departments():
    return jsonify([department.to_dict() for department in Department.query])
