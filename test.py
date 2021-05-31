import json
import unittest
from unittest.mock import patch
from run import app


DEPARTMENTS_MOCK = [
    {'name': 'gally', 'department': 'hotel', 'salary': 1200},
    {'name': 'hotel', 'department': 'gally', 'salary': 1600}
]


class MainViewCase(unittest.TestCase):
    @patch('app.main.resp_json', return_value=DEPARTMENTS_MOCK)
    def test_departments_with_mock(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/departments')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('hotel', str(resp.data))


    def test_api(self):
        client = app.test_client()
        resp = client.get('/api')
        self.assertEqual(resp.status_code, 200)


class ApiViewCase(unittest.TestCase):
    def test_all_departments(self):
        client = app.test_client()
        resp = client.get('/api/departments')
        self.assertEqual(resp.status_code, 200)

    def test_all_employees(self):
        client = app.test_client()
        resp = client.get('/api/employees')
        self.assertEqual(resp.status_code, 200)

    def test_get_employee(self):
        client = app.test_client()
        resp_ok = client.get('/api/employees/5')
        resp_bad = client.get('/api/employees/999')
        self.assertEqual(resp_ok.status_code, 200)
        self.assertNotEqual(resp_bad.status_code, 200)

    # # this test makes effects on db:
    # def test_create_employee_with_db(self):
    #     client = app.test_client()
    #     data = {
    #         'first_name': 'Vasyl',
    #         'last_name': 'Melnik',
    #         'salary': 1700,
    #         'department_id': 1
    #     }
    #     resp = client.post('/api/employees', data=json.dumps(data), content_type='application/json')
    #     self.assertEqual(resp.status_code, 201)

    def test_create_employee_with_mock(self):
        with patch('app.db.session.add') as session_add_mock, \
                patch('app.db.session.commit') as session_commit_mock:
            client = app.test_client()
            data = {
                'first_name': 'Mock',
                'last_name': 'Melnik',
                'salary': 1700,
                'department_id': 1
            }
            resp = client.post('/api/employees', data=json.dumps(data), content_type='application/json')
            session_add_mock.assert_called_once()
            session_commit_mock.assert_called_once()

    # # this test makes effects on db
    # def test_delete_employee(self):
    #     client = app.test_client()
    #     resp = client.delete('api/employees/11')
    #     self.assertEqual(resp.status_code, 204)


if __name__ == '__main__':
    unittest.main()
