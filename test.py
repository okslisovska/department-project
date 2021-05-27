import unittest
from unittest.mock import patch
from run import app


DEPARTMENTS_MOCK = [{'name': 'gally'}, {'name': 'hotel'}]

class MainViewCase(unittest.TestCase):
    @patch('app.main.resp_json', autospec=True, return_value=DEPARTMENTS_MOCK)
    def test_departments_mock(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/departments')
        mock_db_call.assert_called_once()
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
        resp_bad = client.get('/api/employees/1')
        self.assertEqual(resp_ok.status_code, 200)
        self.assertNotEqual(resp_bad.status_code, 200)


if __name__ == '__main__':
    unittest.main()
