from datetime import date
from app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    employees = db.relationship('Employee', backref='department', lazy=True)

    def __repr__(self):
        return f"Department({self.name})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            }


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    def __repr__(self):
        return f"Employee({self.first_name} {self.last_name} {self.birthday} {self.department.name} {self.salary})"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'salary': self.salary,
            'birthday': self.birthday.isoformat(),
            'department': self.department.name
            }
