import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health_route(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()