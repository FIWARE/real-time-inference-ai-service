from app import __version__
from app.config import settings
from app.schemas.health import Health
from classification_model import __version__ as model_version
from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health", response_model=Health, status_code=200)
def health() -> dict:
	health = Health(
		name=settings.PROJECT_NAME, api_version=__version__, model_version= model_version
	)

	return health.dict()

