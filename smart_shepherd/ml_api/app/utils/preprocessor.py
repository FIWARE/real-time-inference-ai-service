from typing import List

import pandas as pd
import requests
from app.config import config
from classification_model.processing.validation import MultipleAnimalDataInputs
from fastapi.encoders import jsonable_encoder


class Preprocessor: 
	def notification_parser(self, payload: dict):
		"""
		Extracts animal id and coordinates from the notification payload.
		"""

		list = payload["data"]
		id = list[0]["id"]
		location = list[0]["location"]["value"]
		coordinates = location["coordinates"]

		return id, coordinates

	def temperature_parser(self) -> float:
		""" 
		Gets temperature data and parses it.
		"""

		orion = config.WEATHER_SERVICE_ORION_HOST
		port = config.WEATHER_SERVICE_ORION_PORT
		sensor_id = config.TEMPERATURE_SENSOR_ID
		url = f"http://{orion}:{port}/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:{sensor_id}"
		HEADER = {"Content-Type": "application/json"}

		try:
			response = requests.request("GET", url, headers=HEADER)
		except requests.HTTPError as e:
			if e.response.status_code == 404:
				return e

		json_response = response.json()
		temperature = json_response["temperature"]["value"]

		return temperature

	def model_input_preprocessor(
			self, coordinates:List[float], temperature: float
		):
		""" 
		Appends the temperature to the coordinates list.
		Makes list compatiable with the pydantic trained model input format.
		""" 
		coordinates.append(temperature)
		data = coordinates

		input = {
				"inputs" : [
					{
						"pos_x": data[0],
						"pos_y": data[1],
						"pos_z": data[2],
						"temp": data[3]
					}   
				]
			}

		input = MultipleAnimalDataInputs(**input)
		model_input = pd.DataFrame(data=jsonable_encoder(input.inputs))

		return model_input


preprocessor = Preprocessor()
