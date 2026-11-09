"""Create the FastAPI application and register HTTP routes."""

from fastapi import FastAPI

from backend.controllers.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="RepoGuide", version="0.1.0")
    app.include_router(health_router)
    return app


app = create_app()
