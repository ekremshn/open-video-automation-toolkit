from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_when_ffmpeg_is_available() -> None:
    completed_process = Mock()
    completed_process.returncode = 0
    completed_process.stdout = "ffmpeg version 7.1 Copyright\n"

    with patch("app.main.subprocess.run", return_value=completed_process):
        response = client.get("/health")

    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "ok"
    assert body["ffmpeg_available"] is True
    assert body["ffmpeg_version"] == "7.1"


def test_health_when_ffmpeg_is_missing() -> None:
    with patch(
        "app.main.subprocess.run",
        side_effect=FileNotFoundError,
    ):
        response = client.get("/health")

    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "ok"
    assert body["ffmpeg_available"] is False
    assert body["ffmpeg_version"] is None


def test_health_when_ffmpeg_returns_error() -> None:
    completed_process = Mock()
    completed_process.returncode = 1
    completed_process.stdout = ""

    with patch("app.main.subprocess.run", return_value=completed_process):
        response = client.get("/health")

    body = response.json()

    assert response.status_code == 200
    assert body["ffmpeg_available"] is False
    assert body["ffmpeg_version"] is None


def test_create_and_read_job() -> None:
    payload = {
        "topic": "A calm nature video",
        "orientation": "portrait",
        "duration_seconds": 30,
        "subtitles_enabled": True,
        "voice": "tr-TR-EmelNeural",
    }

    create_response = client.post("/render/jobs", json=payload)

    assert create_response.status_code == 202

    job_id = create_response.json()["job_id"]
    status_response = client.get(f"/render/jobs/{job_id}")

    assert status_response.status_code == 200
    assert status_response.json()["status"] == "accepted"


def test_invalid_duration() -> None:
    response = client.post(
        "/render/jobs",
        json={"topic": "Test video", "duration_seconds": 2},
    )

    assert response.status_code == 422
