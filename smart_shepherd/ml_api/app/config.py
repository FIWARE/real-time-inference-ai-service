import os

from pydantic import BaseSettings


class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"
	PROJECT_NAME = "Animal Activity Prediction API"


settings = Settings()

class ProcessorConfig:
	# Real Time Weather Orion host 
	WEATHER_SERVICE_ORION_HOST = os.environ["WEATHER_SERVICE_ORION_HOST"]
	# Real Time Weather Orion port
	WEATHER_SERVICE_ORION_PORT = os.environ["WEATHER_SERVICE_ORION_PORT"]
	# for simplification reasons, temperature sensor id is constant
	TEMPERATURE_SENSOR_ID = "001"
	# Smart Shepherd Orion host 
	AI_PROVIDER_ORION_HOST = os.environ["AI_PROVIDER_ORION_HOST"]
	# Smart Shepherd Orion port
	AI_PROVIDER_ORION_PORT = os.environ["AI_PROVIDER_ORION_PORT"]	


config = ProcessorConfig()

