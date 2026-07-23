from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Open Video Automation Toolkit",
    description="API service for creating and tracking automated video rendering jobs.",
    version="0.1.0",
)


class RenderJobRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=200)
    orientation: str = Field(default="portrait", pattern="^(portrait|landscape)$")
    duration_seconds: int = Field(default=30, ge=5, le=600)
    subtitles_enabled: bool = True
    voice: str | None = None


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "Open Video Automation Toolkit",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/render/jobs")
def create_render_job(request: RenderJobRequest) -> dict:
    return {
        "status": "accepted",
        "message": "Render job accepted for processing.",
        "job": request.model_dump(),
    }
