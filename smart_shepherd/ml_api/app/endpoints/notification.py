from app.utils.postprocessor import postprocessor
from app.utils.preprocessor import preprocessor
from classification_model.predict import make_prediction
from fastapi import APIRouter, Body

router=APIRouter(tags=["Notification"])

@router.post("/notification")
def receive_notification(data :dict = Body(...)):
	print("This is the current notification payload:")
	print(data)
	# get animal id and coordinates
	id, coordinates = preprocessor.notification_parser(data)
	# get weather data
	temperature = preprocessor.temperature_parser()
	# prepare the model input 
	model_input = preprocessor.model_input_preprocessor(coordinates, temperature)
	# make prediction
	results = make_prediction(input_data=model_input)
	print("This is the prediction result:")
	print(results)
	# postprocessing 
	prediction = postprocessor.prediction_parser_to_ngsild(results)
	postprocessor.update_prediction(id, prediction)

	return results


