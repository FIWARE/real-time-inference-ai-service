# Real Time Weather 

Real Time Weather Ltd. is a weather data provider, operating weather measurement stations all over the world. It allows to query current and historic weather data for specific GPS coordinates.
By means of having a Context Broker deployed in their environement, it enables them to share the data in NGSI-LD format with other organisations to ensure interoperability and standardisation of their services. 

## Deployment 

A **docker compose** file is provided for deploying all the necessary components. 

This setup contains a default configuration via **environment variables** in the docker-compose.yaml file. No further configuration is required, but changes can be made when the setup differs. 

In the root directory of the repository (real_time_weather) run:

```
docker-compose up -d 
````










