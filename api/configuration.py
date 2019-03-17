"""Configuration."""
import os

import dotenv
from pydantic import BaseModel

dotenv.load_dotenv()


class BaseConfig(BaseModel):
    """Base configuration."""

    API_NAME: str = "Test-API"
    API_PREFIX: str = "/api/v1"
    OPENAPI_URL: str = "openapi.json"
    DOCS_URL: str = "docs"
    REDOC_URL: str = "redocs"
    DEBUG: bool = False
    TESTING: bool = False
    PRODUCTION: bool = False
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    VERSION: str = open(os.path.join(BASE_DIR, "VERSION")).read().strip()


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG: bool = True
    TESTING: bool = True
    PRODUCTION: bool = False


class TestConfig(BaseConfig):
    """Test configuration."""

    DEBUG: bool = True
    TESTING: bool = True
    PRODUCTION: bool = False


class ProductionConfig(BaseConfig):
    """Production configuration."""

    DEBUG: bool = False
    TESTING: bool = False
    PRODUCTION: bool = True


def from_envvar():
    """Get configuration class from environment variable."""
    options = {
        "development": DevelopmentConfig,
        "test": TestConfig,
        "production": ProductionConfig,
    }
    try:
        choice = os.environ["ENV"]
    except KeyError:
        raise KeyError("'ENV' is not set")
    if choice not in options:
        msg = "ENV={} is not valid, must be one of {}".format(choice, set(options))
        raise ValueError(msg)
    loaded_config = options[choice](**os.environ)
    return dict(loaded_config)
