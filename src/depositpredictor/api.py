from contextlib import asynccontextmanager
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from loguru import logger

from depositpredictor.mapper import ModelInputFeaturesMapper
from depositpredictor.model import DepositFeatures
from depositpredictor.predictor import DepositPredictorModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application")
    app.state.model = DepositPredictorModel()
    yield
    logger.info("Shutting down application...")

app = FastAPI(title="Bank Predictor", lifespan=lifespan)

@app.get("/health")
async def healthcheck() -> Response:
    return Response(status_code=200)

@app.post("/predict")
async def predict(features: DepositFeatures) -> JSONResponse:
    model: DepositPredictorModel = app.state.model
    data = ModelInputFeaturesMapper.to_input_features(features)
    prediction_result = model.predict(data)
    return JSONResponse(content=prediction_result.model_dump(), status_code=200)
