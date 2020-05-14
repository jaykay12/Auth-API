from service.api import authapp
import unittest, json

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
        response = self.app.get('/oauth/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data())["developer"], "Jalaz Kumar")

    def test_facebook_oauth(self):
        response = self.app.get('/oauth/authorize/facebook')
        self.assertEqual(response.status_code, 302)

    # def test_twitter_oauth(self):
    #     response = self.app.get('/oauth/authorize/twitter')
    #     self.assertEqual(response.status_code, 302)

    def test_github_oauth(self):
        response = self.app.get('/oauth/authorize/github')
        self.assertEqual(response.status_code, 302)

    def test_google_oauth(self):
        response = self.app.get('/oauth/authorize/google')
        self.assertEqual(response.status_code, 302)

    def test_linkedin_oauth(self):
        response = self.app.get('/oauth/authorize/linkedin')
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unitest.main()
