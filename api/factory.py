"""Setup for the Flask application."""
import logging.config
import os

import requests
import urllib3
from fastapi import FastAPI
from redis import Redis

from api import configuration


def create_app():
    """App factory."""
    config = configuration.from_envvar()
    app = FastAPI(
        title=config["API_NAME"],
        version=config["VERSION"],
        openapi_url=f'{config["API_PREFIX"]}/{config["OPENAPI_URL"]}',
        docs_url=f'{config["API_PREFIX"]}/{config["DOCS_URL"]}',
        redoc_url=f'{config["API_PREFIX"]}/{config["REDOC_URL"]}',
    )
    app.config = config

    setup_requests(app)
    setup_logger(app)
    setup_redis(app)
    setup_routes(app)

    return app


def setup_logger(app):
    """Set up the logger."""
    logging.config.fileConfig("logging.conf")
    app.logger = logging.getLogger(app.config["API_NAME"])


def setup_redis(app):
    """Set up a Redis client."""
    app.redis = Redis(
        host=app.config["REDIS_HOST"],
        port=app.config["REDIS_PORT"],
        db=app.config["REDIS_DB"],
    )


def setup_routes(app):
    """Register routes."""
    from api.routers import basic

    app.include_router(basic.router, prefix=app.config["API_PREFIX"])


def setup_requests(app):
    """Set up a session for making HTTP requests."""
    session = requests.Session()
    session.headers["Content-Type"] = "application/json"
    session.headers["User-Agent"] = app.config["API_NAME"]

    retry = urllib3.util.Retry(total=5, status=2, backoff_factor=0.3)

    retry_adapter = requests.adapters.HTTPAdapter(max_retries=retry)

    session.mount("http://", retry_adapter)
    session.mount("https://", retry_adapter)

    app.requests = session
