from threading import Lock

_jobs: dict[str, dict] = {}
_lock = Lock()


def create_job(job_id: str, payload: dict) -> None:
    with _lock:
        _jobs[job_id] = {
            "status": "accepted",
            "progress": 0,
            "payload": payload,
        }


def get_job(job_id: str) -> dict | None:
    with _lock:
        job = _jobs.get(job_id)
        return dict(job) if job else None
