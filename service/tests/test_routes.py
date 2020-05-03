from service.api import authapp,db
import unittest

class TESTSAPI(unittest.TestCase):

    def setUp(self):
        authapp.config['TESTING'] = True
        self.app = authapp.test_client()

    def tearDown(self):
        pass

    def test_base(self):
        response = self.app.get('/api/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unitest.main()
