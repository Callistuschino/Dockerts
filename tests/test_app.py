import unittest
from dockerts.app import create_app


class DockertsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True})
        self.client = self.app.test_client()

    def test_root_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["name"], "dockerts")
        self.assertEqual(data["status"], "running")
        self.assertIn("endpoints", data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("uptime_seconds", data)
        self.assertIn("timestamp", data)

    def test_info_endpoint(self):
        response = self.client.get("/info")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("python_version", data)
        self.assertIn("hostname", data)
        self.assertIn("platform", data)


if __name__ == "__main__":
    unittest.main()
