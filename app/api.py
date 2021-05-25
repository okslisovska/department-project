from flask import Blueprint, jsonify
from app.models import Department, Employee


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/employees/<int:id>')
def get_employee(id):
    return jsonify(Employee.query.get_or_404(id).to_dict())


@bp.route('/departments')
def get_departments():
    return jsonify([department.to_dict() for department in Department.query])
