import json

import requests
from app.config import config
from app.schemas.predict import PredictionResults


class PostProcessor: 
	def prediction_parser_to_ngsild(self, data: PredictionResults):
		"""
		Parses the prediction result to get the prediction.
		Transforms prediction to ngsild payload specification.
		"""

		prediction = data.get("predictions")
		prediction = {
			"animalActivity": {
				"type": "Property",
				"value": prediction
			}
		}
			
		return prediction

	def update_prediction(self, id, ngsild_prediction):
		"""
		Updates the prediction attribute "animalActivity" in the 
		Context Broker of Happy Cattle
		"""

		orion = config.AI_PROVIDER_ORION_HOST
		port = config.AI_PROVIDER_ORION_PORT
		HEADER = {"Content-Type": "application/json"}
		url = f"http://{orion}:{port}/ngsi-ld/v1/entities/{id}/attrs"

		response = requests.request("POST", url=url, headers=HEADER, data=json.dumps(ngsild_prediction))

		return response.text
	

postprocessor = PostProcessor()
