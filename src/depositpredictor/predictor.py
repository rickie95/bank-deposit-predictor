from typing import TypedDict
from loguru import logger
from pandas import DataFrame

from pydantic import BaseModel
from xgboost import XGBClassifier


class InputData(TypedDict):
    """
    Model the input data required for the model in a TypedDict. 
    Some fields have been encoded with one-hot encoding, that prevents the use 
    of Enums, or at least it makes it difficul to implement without intriducing bugs.
    """
    age: int
    education: int
    default: bool
    balance: float
    housing: bool
    loan: bool
    duration: float
    campaign: float
    pdays: float
    previous: float
    job_blue_collar: bool
    job_entrepreneur: bool
    job_housemaid: bool
    job_management: bool
    job_retired: bool
    job_self_employed: bool
    job_services: bool
    job_student: bool
    job_technician: bool
    job_unemployed: bool
    job_unknown: bool
    marital_married: bool
    marital_single: bool
    contact_telephone: bool
    contact_unknown: bool

class PredictionResult(BaseModel):
    might_open: bool

class DepositPredictorModel:

    def __init__(self):
        self.model = XGBClassifier()
        logger.info("Loading model from disk...")
        self.model.load_model("./models/xgboost/current.json")
        logger.info("Model ready")

    def predict(self, data: InputData) -> PredictionResult:
        df = DataFrame(data, index=None)
        df.rename(columns={
            "job_self_employed": "job_self-employed",
            "job_blue_collar": "job_blue-collar"
        })
        result: list[int] = self.model.predict(data)

        return PredictionResult(might_open=bool(result[0]))
