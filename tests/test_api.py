import unittest

from fastapi.testclient import TestClient

from depositpredictor.api import app


class EndpointTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)
        return super().setUp()

    def test_health(self):
        resp = self.client.get("/health")

        self.assertEqual(resp.status_code, 200)
