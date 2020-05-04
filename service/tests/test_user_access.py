from service.api import authapp, db
import unittest
import json

class BaseTest(unittest.TestCase):
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

class TEST_USER_ACCESS(BaseTest):
    def setUp(self):
        userinfo = { "id": "75654", "username": "jalaz.kumar", "password": "jalaz" }
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)

    def tearDown(self):
        pass

    def test_user_access_success(self):
        response = self.app.get('/api/users/75654')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data())["username"],"jalaz.kumar")

    def test_user_access_failure(self):
        response = self.app.get('/api/users/75653')
        self.assertEqual(response.status_code, 400)
