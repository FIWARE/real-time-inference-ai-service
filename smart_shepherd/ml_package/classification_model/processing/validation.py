from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from classification_model.config.core import config
from pydantic import BaseModel, ValidationError


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    validated_data = input_data[config.model_config.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleAnimalDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class AnimalDataInputSchema(BaseModel):
    pos_x: Optional[float]
    pos_y: Optional[float]
    pos_z: Optional[float]
    temp: Optional[float]


class MultipleAnimalDataInputs(BaseModel):
    inputs: List[AnimalDataInputSchema]
