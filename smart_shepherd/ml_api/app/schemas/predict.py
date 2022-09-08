from typing import Any, List, Optional

from classification_model.processing.validation import AnimalDataInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
	predictions : Optional[List[str]]
	version: str
	errors: Optional[Any]


class MultipleAnimalDataInputs(BaseModel):
	inputs: List[AnimalDataInputSchema]

	class Config:
		schema_extra = {
			"example" : {
				"inputs" : [
					{
						"pos_x": 1.22534,
						"pos_y": 2.76543,
						"pos_z": 8.44318,
						"temp": 19.3
					}   
				]
			}
		}
