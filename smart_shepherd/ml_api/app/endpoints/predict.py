import json
from typing import Any

import pandas as pd
from app.schemas.predict import MultipleAnimalDataInputs, PredictionResults
from classification_model.predict import make_prediction
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger

router = APIRouter(tags=["Prediction"])

@router.post("/predict", status_code=200, response_model=PredictionResults)
def predict(input_data: MultipleAnimalDataInputs) -> Any:
	"""
	Make animal activity prediction with the classification model
	"""

	# convert a data type (like a Pydantic model) to something compatible 
	# with JSON (like a dict, list, etc).
	inputs = pd.DataFrame(data=jsonable_encoder(input_data.inputs))
	logger.info(f"Making prediction on inputs: {input_data.inputs}")
	results = make_prediction(input_data=inputs)

	if results["errors"] is not None:
		logger.warning(f"Prediction validation error: {results.get('errors')}")
		raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

	logger.info(f"Prediction results: {results.get('predictions')}")

	return results
