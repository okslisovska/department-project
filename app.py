import requests
from flask import Flask, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    employees = db.relationship('Employee', backref='department', lazy=True)

    def __repr__(self):
        return f"Department({self.name})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
            }

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    def __repr__(self):
        return f"Employee({self.first_name} {self.last_name} : {self.salary})"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'salary': self.salary,
            'department': self.department.name
            }


@app.route('/')
def index():
    return "<h1>Department-project</h1><p>will be here soon</p>"

@app.route('/departments')
def departments():
    response = requests.get("http://localhost:5000/api/departments")
    return response.text

@app.route('/api/employees/<int:id>')
def get_employee(id):
    return Employee.query.get_or_404(id).to_dict()

@app.route('/api/departments')
def get_departments():
    return jsonify([department.to_dict() for department in Department.query])


if __name__ == "__main__":
    app.run(debug=True)


