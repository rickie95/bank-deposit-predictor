import unittest
from unittest.mock import MagicMock

from fastapi.testclient import TestClient
import pytest

from depositpredictor.api import app
from depositpredictor.model import ContactType, JobType, MaritalStatus
from depositpredictor.predictor import PredictionResult

# @pytest.fixture
# def client():
#     app.state.model = MagicMock()
#     app.state.model.return_value = PredictionResult.POSITIVE
#     with TestClient(app) as c:
#         yield c

class EndpointTest(unittest.TestCase):

    def setUp(self):
        self.model_mock = MagicMock()
        app.state.model = self.model_mock
        self.client = TestClient(app=app)
        return super().setUp()

    def test_health(self):
        resp = self.client.get("/health")

        self.assertEqual(resp.status_code, 200)

    def test_predict(self):
        app.state.model.predict.return_value = PredictionResult(might_open=True)
        features = {
            "age": 21,
            "job": JobType.BLUE_COLLAR.value,
            "education": 2,
            "married": MaritalStatus.MARRIED.value,
            "contact": ContactType.TELEPHONE.value,
            "default": False,
            "balance": 100000,
            "housing": True,
            "loan": False,
            "duration": 2,
            "campaign": 1,
            "pdays": -1,
            "previous": -1
        }

        resp = self.client.post(
            "/predict", 
            json=features
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"might_open": True})

    def test_predict_will_answer_422_with_invalid_input(self):
        features = {
            "age": 21,
            "job": JobType.BLUE_COLLAR.value,
            "education": 2
        }

        resp = self.client.post(
            "/predict", 
            json=features
        )

        self.assertEqual(resp.status_code, 422)
