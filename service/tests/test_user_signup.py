from service.api import authapp
import unittest
import json

class TESTS_USER_SIGNUP(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        authapp.config['TESTING'] = True
        self.app = authapp.test_client()

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_usersignup_success(self):
        userinfo = { "id": "75655", "username": "jalaz.kumar", "password": "jalaz" }
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.get_data())["username"],userinfo["username"])

    def test_usersignup_duplicate(self):
        userinfo = { "id": "75652", "username": "jalaz.kumar", "password": "jalaz" }
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        userinfo = { "id": "75652", "username": "jalaz.kumar", "password": "jalaz" }
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        self.assertEqual(response.status_code, 503)

    def test_usersignup_empty(self):
        userinfo = {}
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        self.assertEqual(response.status_code, 400)

    def test_usersignup_missing(self):
        headers = { 'Content-Type': 'application/json'}
        userinfo = {"username": "jalaz.kumar", "password": "jalaz"}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        self.assertEqual(response.status_code, 400)
        userinfo = {"id": "75655", "password": "jalaz"}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        self.assertEqual(response.status_code, 400)
        userinfo = {"id": "75655", "username": "jalaz.kumar"}
        response = self.app.post('/api/users', headers = headers, json=userinfo)
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unitest.main()
