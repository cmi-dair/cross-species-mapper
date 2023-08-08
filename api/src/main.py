"""Main module for the API."""
import logging

import fastapi
from fastapi.middleware import cors
from src.core import settings
from src.routers.features import views as feature_views
from src.routers.surfaces import views as surface_views

config = settings.get_settings()
LOGGER_NAME = config.LOGGER_NAME

settings.initialize_logger()
logger = logging.getLogger(LOGGER_NAME)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

api = fastapi.APIRouter(prefix="/api")
api.include_router(feature_views.router)
api.include_router(surface_views.router)

logger.info("Starting API.")
app = fastapi.FastAPI()
app.include_router(api)

logger.info("Adding CORS middleware.")
app.add_middleware(
    cors.CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
