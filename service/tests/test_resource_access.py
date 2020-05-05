from service.api import authapp
import unittest
import json, base64

class TESTS_RESOURCE_ACCESS(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        authapp.config['TESTING'] = True
        self.app = authapp.test_client()
        userinfo = { "id": "75656", "username": "jalaz.kumar", "password": "jalaz" }
        headers = { 'Content-Type': 'application/json'}
        response = self.app.post('/api/users', headers = headers, json=userinfo)

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def token_creation(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('jalaz.kumar:jalaz').encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/token', headers = headers)
        return json.loads(response.get_data())["token"]

    def test_resourceaccess_password_success(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('jalaz.kumar:jalaz').encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/resource', headers = headers)
        self.assertEqual(response.status_code, 200)

    def test_resourceaccess_password_failure(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('jalaz.kumar:jalaj').encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/resource', headers = headers)
        self.assertEqual(response.status_code, 401)

    def test_resourceaccess_token_success(self):
        token = self.token_creation()
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('{0}:{1}'.format(token,'jalaz')).encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/resource', headers = headers)
        self.assertEqual(response.status_code, 200)

    def test_resourceaccess_token_failure_password_success(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('{0}:{1}'.format('','jalaz')).encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/resource', headers = headers)
        if response.status_code==401:
            headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('{0}:{1}'.format('jalaz.kumar','jalaz')).encode("utf-8")).decode("utf-8"))}
            response = self.app.get('/api/resource', headers = headers)
            self.assertEqual(response.status_code, 200)

    def test_resourceaccess_token_failure_password_failure(self):
        headers = { 'Authorization': 'Basic {}'.format(base64.b64encode(('{0}:{1}'.format('','jalaj')).encode("utf-8")).decode("utf-8"))}
        response = self.app.get('/api/resource', headers = headers)
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unitest.main()
