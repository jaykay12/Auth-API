from service.api import authapp,db
import unittest

class TESTS_BASE(unittest.TestCase):

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

    def test_intro(self):
        response = self.app.get('/api/')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unitest.main()
