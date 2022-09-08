from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

from classification_model.config.core import config

animal_activity_pipe = Pipeline(
    [
     
    # ======= pre-processing ======
    # Standerdize the coordinates with the standard scaler 
    ("standard_scaler", StandardScaler()),

    # ====== classification model =====
    # xgboost classifier 
    (
		"xgboost_classifier",
		XGBClassifier(
			max_depth=config.model_config.max_depth,
			learning_rate=config.model_config.learning_rate,
			n_estimators=config.model_config.n_estimators,
			verbosity=config.model_config.verbosity,
			objective=config.model_config.objective,
			use_label_encoder=config.model_config.use_label_encoder,
			eval_metric=config.model_config.eval_metric
		)
	)
    ]
)

