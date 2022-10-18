# Classification model Python Package

The Classification model Python package is a collection of modules dedicated to fulfil the following functionalities: Preprocessing, training, configuring training model, adding/updating datasets, validating data. 

Machine learning pipelines helps to automate the ML Workflow and enable to pre-process data, apply transformations and train models. It gives more flexibility to iterate and experiment to reach a better performance of trained models. 

# Usage guide: 

## Configuration 

Under the [config.py](/smart_shepherd/ml_package/classification_model/config/core.py) module the following configurations can be made: 
- The paths and directory names for the trained model, dataset and YAML config file.
- The class for the application config and its attributes. 
- the class for the model config and its attributes(configuration relevant to model
	training and feature engineering).

Under the [config.yml](/smart_shepherd/ml_package/classification_model/config.yml) the values are assigned to the model and app class attributes:
- Package name
- Train and test data file names 
- Pipeline name and output name
- Feature names selected to train the ML model 
- train test split parameters (test size, n_splits, shuffle, random seed)
- ML algorithm parameters (e.g. XGBoost)


## Pipeline 

the module [pipeline.py](/smart_shepherd/ml_package/classification_model/pipeline.py) encapsulates the different stages we like to add to ur data and ML pipeline. 
Here depending on the dataset, different preprocessing stages could be added. 
The same applies in case the data scientist wants to test a different ML algorithm.

## Dataset 

Under the directory [Dataset](/smart_shepherd/ml_package/classification_model/datasets/) the training and testing datasets are located. 
So in case the data scientist wants to change the data, this is where it should be done. 

## Training 

Under the module [train_pipeline.py](/smart_shepherd/ml_package/classification_model/train_pipeline.py), the training dataset is loaded, then transformed to a dataframe, 
split into train and test set. 

To start the training, simply execute the following command: 
```
python train_pipeline.py
```
When the the training ends, the trained pipeline will be saved, in the directory "trained_models"

## Prediction 

The module [predict.py](/smart_shepherd/ml_package/classification_model/predict.py) is used to make new predictions with test data. 

To run the prediction, simply execute the following command: 

```
python predict.py
```


