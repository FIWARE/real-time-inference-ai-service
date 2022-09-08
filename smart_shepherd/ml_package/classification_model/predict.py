import typing as t

import pandas as pd

from classification_model import __version__ as _version
from classification_model.config.core import config
from classification_model.processing.data_manager import (load_encoder,
                                                          load_pipeline)
from classification_model.processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_animal_activity_pipe = load_pipeline(file_name=pipeline_file_name)

encoder_file_name = f"{config.app_config.encoder_save_file}{_version}.pkl"
_encoder = load_encoder(file_name=encoder_file_name)

# creating optional type hints with typing.Union 
# which makes the expected input to be either a dataframe or dict
def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = _animal_activity_pipe.predict(
            X=validated_data[config.model_config.features]
        )
        readable_predictions = _encoder.inverse_transform(predictions)
        results = {
            "predictions": [pred for pred in readable_predictions], 
            "version": _version,
            "errors": errors,
        }

    return results
