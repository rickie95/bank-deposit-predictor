import unittest
from unittest.mock import MagicMock, patch, Mock

from depositpredictor.predictor import DepositPredictorModel
from unittest.mock import patch


class DepositPredictorTest(unittest.TestCase):

    @patch('depositpredictor.predictor.XGBClassifier')
    def test_init(self, classifier_mock: Mock):
        instance_mock = MagicMock()
        classifier_mock.return_value = instance_mock
        instance_mock.load_model.return_value = None

        predictor = DepositPredictorModel()

        self.assertEqual(predictor.model, instance_mock)
        instance_mock.load_model.assert_called_once_with("./models/xgboost/current.json")

    @patch('depositpredictor.predictor.XGBClassifier')
    def test_init_fails_to_load(self, classifier_mock: Mock):
        instance_mock = MagicMock()
        classifier_mock.return_value = instance_mock
        instance_mock.load_model.side_effect = FileNotFoundError()

        with self.assertRaises(FileNotFoundError):
            DepositPredictorModel()
            instance_mock.load_model.assert_called_once_with("./models/xgboost/current.json")
