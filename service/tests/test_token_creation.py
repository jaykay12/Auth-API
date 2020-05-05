from service.api import authapp
import unittest
import json, base64

class TESTS_TOKEN_CREATION(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        authapp.config['TESTING'] = True
        self.app = authapp.test_client()
        userinfo = { "id": "75654", "username": "jalaz.kumar", "password": "jalaz" }
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tokencreation_success(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('jalaz.kumar:jalaz').encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/token', headers = headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data())["duration"], 600)

    def test_tokencreation_failure(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('jalaz.kumar:jalaj').encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/token', headers = headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_data().decode(), "Unauthorized Access")

if __name__ == "__main__":
    unitest.main()
