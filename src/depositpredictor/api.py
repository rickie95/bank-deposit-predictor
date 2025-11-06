from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

from depositpredictor.mapper import ModelInputFeaturesMapper
from depositpredictor.model import DepositFeatures
from depositpredictor.predictor import DepositPredictorModel

app = FastAPI(title="Bank Predictor")


@app.get("/health")
def healthcheck():
    return Response(status_code=200)

@app.get("/predict")
def predict(features: DepositFeatures) -> JSONResponse:
    model = DepositPredictorModel()
    data = ModelInputFeaturesMapper.to_input_features(features)
    prediction_result = model.predict(data)
    return JSONResponse(content=prediction_result, status_code=200)
