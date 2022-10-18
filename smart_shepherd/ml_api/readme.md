# ML API as a service

The ML model is deployed via REST API to be consumed for real-time inference. 
The implementation of the ML API relies on [FastAPI](https://fastapi.tiangolo.com/).

FastAPI is a modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Architecture 
The architecture below illustrates a high level overview of the ML API and how it works. 

![ml-api-architecture](/doc/architectures-ml-api.jpg)

When the AI service receives a notification in the [/notification endpoint](/smart_shepherd/ml_api/app/endpoints/notification.py) (based on the subscription to receive new animal coordinates) the following steps are happening: 

- Parsing the notification payload and extracting the animal ID and coordinates. 
- Get weather data. 
- transform the data (x,y,z coordinates and temperature) to the proper model input format. 
- Making prediction with the trained model. 
- Transform the prediction model output to NGSI-LD.
- Update prediction attribute in the context broker of Smart Shepherd.  

# API documentation

Since the ML API is built based on [FastAPI](https://fastapi.tiangolo.com/), the API documentation can be accessible under this url: http://localhost:5000/docs
and we should have something as shown in the figure below. 

![API documentation](/doc/api-doc.png)



