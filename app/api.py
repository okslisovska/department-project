from datetime import date
from flask import Blueprint, jsonify, request
from app import db
from app.models import Department, Employee


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/departments')
def all_departments():
    return jsonify([department.to_dict() for department in Department.query])


@bp.route('/employees')
def all_employees():
    return jsonify([employee.to_dict() for employee in Employee.query])


@bp.route('/employees/<int:id>')
def get_employee(id):
    return jsonify(Employee.query.get_or_404(id).to_dict())


@bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee = Employee(
        first_name=data['first_name'],
        last_name=data['last_name'],
        salary=data['salary'],
        birthday=date.fromisoformat(data['birthday']),
        department_id=data['department_id']
    )
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Created successfully'}), 201


@bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    employee = Employee.query.get_or_404(id)
    employee.first_name = data['first_name']
    employee.last_name = data['last_name']
    employee.salary = data['salary']
    employee.department_id = data['department_id']
    db.session.commit()
    return jsonify({'message': 'Updated successfully'})


@bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 204
