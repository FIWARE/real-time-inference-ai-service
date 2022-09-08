# Happy Cattle 

HappyCattle Co. is a big farm raising animals of different kinds. They have setted up an IOT system and installed a farm management system that creates a digital twin of their animals in the farm. Now, they want to extend its functionality to recognize the animal activity they are raising. Therefore, they decided to rely on the AI technology to gain insights from their data collected from their IOT farming system. 

They will acquire the offering of the AI service of Smart Shepherd Inc. for animal activity recognition.  
By providing data about the animal coordinates in the x,y, z axis and labels consisting of the different animal activities (e.g Grazing, Stand up, Sternal lying, Walking, Licking calf,...), the AI service provider company could train a ML model and set up the inference system to use the service in production (the focus of this tutorial).


## Deployment 

A **docker compose** file is provided for deploying all the necessary components. 

This setup contains a default configuration via **environment variables** in the docker-compose.yaml file. No further configuration is required, but changes can be made when the setup differs. 

In the root directory of the repository (happy_cattle) run:

```
docker-compose up -d 
````
