from typing import Literal

from pydantic import BaseModel, Field


class RenderJobRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=200)
    orientation: Literal["portrait", "landscape"] = "portrait"
    duration_seconds: int = Field(default=30, ge=5, le=600)
    subtitles_enabled: bool = True
    voice: str | None = Field(default=None, max_length=100)


class RenderJobResponse(BaseModel):
    job_id: str
    status: str
    message: str
    job: RenderJobRequest


class RenderJobStatus(BaseModel):
    job_id: str
    status: str
    progress: int = Field(ge=0, le=100)
