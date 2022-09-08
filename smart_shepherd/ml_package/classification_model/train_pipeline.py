from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder

from config.core import config
from pipeline import animal_activity_pipe
from processing.data_manager import load_dataset, save_encoder, save_pipeline


def run_training() -> None:
	"""Train the model."""

	# read training data
	data = load_dataset(file_name=config.app_config.training_data_file)

	X = data[config.model_config.features] #predictors 
	y = data[config.model_config.target] #target

	# encode target
	enc = LabelEncoder()
	enc.fit(y)
	y = enc.transform(y) 
	save_encoder(encoder_to_persist=enc)

	# divide train and test
	kfold = StratifiedKFold(
		n_splits=config.model_config.n_splits,
		shuffle=config.model_config.shuffle,
		random_state=config.model_config.random_state)

	for train_ix, test_ix in kfold.split(X, y):
		X_train, X_test = X.iloc[train_ix], X.iloc[test_ix]
		y_train, y_test = y[train_ix], y[test_ix]


	# fit model
	animal_activity_pipe.fit(X_train,y_train)

	# persist trained model
	save_pipeline(pipeline_to_persist=animal_activity_pipe)


if __name__ == "__main__":
    run_training()
