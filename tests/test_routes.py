# tests/test_routes.py
import unittest
from main import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/politica-de-privacidad')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/terminos-de-uso')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
