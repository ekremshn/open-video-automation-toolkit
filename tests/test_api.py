from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


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
