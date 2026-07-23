import subprocess
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, HTTPException

from app.config import settings
from app.models import RenderJobRequest, RenderJobResponse, RenderJobStatus
from app.store import create_job, get_job


app = FastAPI(
    title="Open Video Automation Toolkit",
    description="API service for creating and tracking automated video rendering jobs.",
    version="0.1.0",
)


@app.on_event("startup")
def startup() -> None:
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    settings.temp_dir.mkdir(parents=True, exist_ok=True)


def get_ffmpeg_status() -> tuple[bool, str | None]:
    try:
        result = subprocess.run(
            [settings.ffmpeg_path, "-version"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (FileNotFoundError, PermissionError, subprocess.TimeoutExpired):
        return False, None

    if result.returncode != 0:
        return False, None

    first_line = result.stdout.splitlines()[0] if result.stdout else ""
    version = first_line.removeprefix("ffmpeg version ").split()[0] if first_line else None

    return True, version


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "Open Video Automation Toolkit",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, str | bool | None]:
    ffmpeg_available, ffmpeg_version = get_ffmpeg_status()

    return {
        "status": "ok",
        "environment": settings.app_env,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ffmpeg_available": ffmpeg_available,
        "ffmpeg_version": ffmpeg_version,
    }


@app.post("/render/jobs", response_model=RenderJobResponse, status_code=202)
def create_render_job(request: RenderJobRequest) -> RenderJobResponse:
    job_id = uuid4().hex
    create_job(job_id, request.model_dump())

    return RenderJobResponse(
        job_id=job_id,
        status="accepted",
        message="Render job accepted for processing.",
        job=request,
    )


@app.get("/render/jobs/{job_id}", response_model=RenderJobStatus)
def read_render_job(job_id: str) -> RenderJobStatus:
    job = get_job(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Render job not found.")

    return RenderJobStatus(
        job_id=job_id,
        status=job["status"],
        progress=job["progress"],
    )
