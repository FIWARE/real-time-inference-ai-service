import pandas as pd
import pytest
from app.main import app
from classification_model.config.core import config
from classification_model.processing.data_manager import load_dataset
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture
def test_data() -> pd.DataFrame():
	return load_dataset(file_name=config.app_config.test_data_file)

# see: https://fastapi.tiangolo.com/tutorial/testing/
@pytest.fixture
def client():
	return TestClient(app)

