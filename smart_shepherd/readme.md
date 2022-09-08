# Smart Shepherd 

Smart Shepherd Inc. is offering an AI service which consists of a set of scripts that achieve data processing functionality and inference with the trained AI model. In addition to that, they are deploying as part of their offering an instance of a Context Broker with the MongoDB database associated with it to manage real time data coming from the consumer.

## About the AI service 

The AI service provider is responsible for training a Machine Learning model using historical data as well as providing an interface for the data provisioning needed for the inference to get future prediction based on the right-time data in NGSI-LD format received via the Context Broker. In addition to that, the output of the AI model is also being processed. Then, the prediction attribute(s) are updated in the Context Broker.

![ai-service](/doc/ai-service.jpg)

## Deployment 

A **docker compose** file is provided for deploying all the necessary components. 

This setup contains a default configuration via **environment variables** in the docker-compose.yaml file. No further configuration is required, but changes can be made when the setup differs. 

The following are the important environment variables to configure: 

```
      - WEATHER_SERVICE_ORION_HOST=weather.orion.docker
      - WEATHER_SERVICE_ORION_PORT=1026
      - AI_PROVIDER_ORION_HOST=ai.orion.docker
      - AI_PROVIDER_ORION_PORT=1026
```

In the root directory of the repository (smart_shepherd) run:

```
docker-compose up -d 
````


