# Building real-time inference AI services with FIWARE

[FIWARE Global Summit AI training session materials]

This tutorial is an implementation of a proof of concept for 
an AI service that provids real-time prediction and by means of having a Context Broker deployed in the offered service, the data provisioning will be in real-time from the data source(s) to the AI model and respectively publishing the results of the predictions to the consumer application via a Context Broker on the consumer side.

# Overall architecture 
The architecture below illustrates the environments correspondant to each participant and the componenets that are used to enable the real-time inference. 

**Use case:** Prediction of animal activity (e.g grazing, walking, stand-up,..) based on its x, y, z coordinates and the observed ambinat temperature. 

![architecture](/doc/overall-architecture.jpg)

# Docker setup 

There are three environments of the different participants to be setup:

- Smart Shepherd (AI Service Provider and Data Service Consumer)
- Happy Cattle (AI Service Consumer)
- Real Time Weather (Data Service Provider)

For each, docker compose files are provided.


To ensure the communication between the different containers in each participant's environment, the "ai-poc-network" is a shared network between all of them to enable that. To create this network run the following command: 

```
docker network create ai-poc-network
```

All components of each participant can be deployed by running the following command:

```
docker compose \
 	-f happy_cattle/docker-compose.yml \
	-f smart_shepherd/docker-compose.yml \
	-f real_time_weather/docker-compose.yml \
 	up -d
```
Note: configurations could be made through the environment variables in the docker-compose.yml files under each repository of the participants, in case of set up change. 

# Subscriptions setup

The main goal of te subscription is to allow the automated data exchange between the participants on particular attributes. That will enable the real-time AI inference. 

In this use case, there are three subscriptions to be setup: 

* **Subscription 1:**  Smart Shepehrd Inc. subscribes to the Context Broker of Happy Cattle Co. to receive in an automated way animal coordinates update in its Context Broker by means of a Notification Proxy 

```shell
   curl -v --location POST 'localhost:1029/ngsi-ld/v1/subscriptions/' \
      --header 'Content-Type: application/json' \
      --data-raw ' {
         "description":"Notify me of new animal coordinates",
         "type":"Subscription",
         "name":"animalCoordinatesSubscription",
         "entities":[
            {
               "type":"Animal"
            }
         ],
         "watchedAttributes":["location"],
         "notification":{
            "attributes":["location"],
            "endpoint":{
               "uri":"http://ai.notification-proxy.docker:8080/notification",
               "accept":"application/json"
            }
         }
      }'
  ```
* **Subscription 2:** Smart Shepherd Inc. AI service subscribes to the Context Broker in its own environment, to receive at the notification endpoint the coordinates once it is updated due to subscription 1. That will trigger the calculation of the prediction which also relies on getting temerature data. 

```shell
   curl -v --location POST 'localhost:1028/ngsi-ld/v1/subscriptions/' \
      --header 'Content-Type: application/json' \
      --data-raw ' {
         "description":"Notify AI service of new animal coordinates",
         "type":"Subscription",
         "name":"animalCoordinatesSubscription",
         "entities":[
            {
               "type":"Animal"
            }
         ],
         "watchedAttributes":["location"],
         "notification":{
            "attributes":["location"],
            "endpoint":{
               "uri":"http://apis.docker:5000/notification",
               "accept":"application/json"
            }
         }
      }'
  ```

* **Subscription 3:** Happy Cattle Co. subscribes to receive predictions updates (after inference) from the Context Broker of Smart Shepherd Inc. by means of a Notification Proxy 

```shell
   curl -v --location POST 'localhost:1028/ngsi-ld/v1/subscriptions/' \
      --header 'Content-Type: application/json' \
      --data-raw ' {
         "description":"Notify me of new animal activity prediction",
         "type":"Subscription",
         "name":"predictionSubscription",
         "entities":[
            {
               "type":"Animal"
            }
         ],
         "watchedAttributes":["animalActivity"],
         "notification":{
            "attributes":["animalActivity"],
            "endpoint":{
               "uri":"http://farm.notification-proxy.docker:8081/notification",
               "accept":"application/json"
            }
         }
      }'
  ```

# Example of usage 

* Create a TemperatureSensor entity at the Context Broker of Real Time Weather: 

```shell
   curl -v --location POST 'localhost:1026/ngsi-ld/v1/entities' \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "id":"urn:ngsi-ld:TemperatureSensor:001",
         "type":"TemperatureSensor",
         "dateObserved":{
            "type":"Property",
            "value":"2016-11-30T07:00:00.00Z"
         },
         "temperature":{
            "type":"Property",
            "value":17
         }
      }'
```

* Create an Animal entity at the Contect Broker of Happy Cattle:
```shell
   curl -v --location POST 'localhost:1029/ngsi-ld/v1/entities' \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "id":"urn:ngsi-ld:Animal:0001",
         "type":"Animal",
         "species":{
            "type":"Property",
            "value":"cow"
         },
         "location":{
            "type":"GeoProperty",
            "value":{
               "type":"Point",
               "coordinates":[
                  3.165,
                  2.6133,
                  -1.4292
               ]
            }
         }
      }'
```

* Query Smart Shepherd Broker: 
```shell
   curl --location --request GET 'localhost:1028/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001'
``` 

Here you should have as a result an entity of type Animal created in the Context Broker of Smart Shepherd, due to subscription 1.



* Update a property in the Context Broker of Happy Cattle: 
```shell
   curl -v --location POST 'localhost:1029/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001/attrs' \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "location":{
            "type":"GeoProperty",
            "value":{
               "type":"Point",
               "coordinates":[
                  7.165,
                  3.6133,
                  -1.1292
               ]
            }
         }
      }'
```

After creating the entities or updating them, everytime this process triggers the prediction calculation, first the results are updates in the Context Broker of Smart Shepherd (see entity: AnimalActivity) and then due to subscription 3, this new entity AnimalActiviy is updated in the Context Broker of Happy Cattle.  

* Query the Broker of Smart Shepherd:
 ```shell
   curl --location --request GET 'localhost:1028/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001'
 ``` 

 Result: 

 ```
 {"@context":"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld","id":"urn:ngsi-ld:Animal:0001","type":"Animal","location":{"value":{"type":"Point","coordinates":[4.165,3.6133,-1.1292]},"type":"GeoProperty"},"animalActivity":{"value":"Sternal lying","type":"Property"}} 
 ```

* Query the Broker of Happy Cattle:
 ```shell
   curl --location --request GET 'localhost:1029/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001'
 ``` 

 Result: 

 ```
 {"@context":"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld","id":"urn:ngsi-ld:Animal:0001","type":"Animal","location":{"value":{"type":"Point","coordinates":[4.165,3.6133,-1.1292]},"type":"GeoProperty"},"animalActivity":{"value":"Sternal lying","type":"Property"}} 
 ```

