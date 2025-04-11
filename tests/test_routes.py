import unittest
import sys
import os

# Agregamos el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import create_app  # Importás la factory function


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy(self):
        response = self.client.get("/politica-de-privacidad")
        self.assertEqual(response.status_code, 200)

    def test_terms_of_use(self):
        response = self.client.get("/terminos-de-uso")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()