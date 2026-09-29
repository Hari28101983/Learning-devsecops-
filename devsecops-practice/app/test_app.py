import unittest

from app import response_for


class ResponseTests(unittest.TestCase):
    def test_home_page(self):
        status, payload = response_for("/")

        self.assertEqual(status, 200)
        self.assertEqual(payload["message"], "DevSecOps practice application")

    def test_health_endpoint(self):
        status, payload = response_for("/health")

        self.assertEqual(status, 200)
        self.assertEqual(payload, {"status": "healthy"})

    def test_unknown_path(self):
        status, payload = response_for("/missing")

        self.assertEqual(status, 404)
        self.assertEqual(payload, {"error": "not found"})


if __name__ == "__main__":
    unittest.main()
