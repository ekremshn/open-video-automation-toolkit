# Open Video Automation Toolkit

An open-source automation toolkit for creating, rendering and publishing videos with n8n, FFmpeg and AI services.

## Features

- FastAPI-based rendering API
- Docker and Docker Compose support
- FFmpeg-ready container
- Render job creation and status tracking
- Portrait and landscape video support
- Subtitle configuration
- Environment-variable based configuration
- Health check endpoint
- FFmpeg availability and version reporting
- Automated tests
- GitHub Actions CI
- Issue and pull request templates

## Quick Start

Clone the repository:

```bash
git clone https://github.com/ekremshn/open-video-automation-toolkit.git
cd open-video-automation-toolkit
```

Create the environment file:

```bash
cp .env.example .env
```

Start the application:

```bash
docker compose up --build
```

Open:

- API: `http://localhost:3101`
- Swagger documentation: `http://localhost:3101/docs`
- Health endpoint: `http://localhost:3101/health`

## Example Request

Create a render job:

```bash
curl -X POST "http://localhost:3101/render/jobs" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "A calm nature video",
    "orientation": "portrait",
    "duration_seconds": 30,
    "subtitles_enabled": true,
    "voice": "tr-TR-EmelNeural"
  }'
```

Example response:

```json
{
  "job_id": "example-job-id",
  "status": "accepted",
  "message": "Render job accepted for processing.",
  "job": {
    "topic": "A calm nature video",
    "orientation": "portrait",
    "duration_seconds": 30,
    "subtitles_enabled": true,
    "voice": "tr-TR-EmelNeural"
  }
}
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Returns application information |
| `GET` | `/health` | Returns application and FFmpeg health status |
| `POST` | `/render/jobs` | Creates a new render job |
| `GET` | `/render/jobs/{job_id}` | Returns render job status |

## Health Check Example

```json
{
  "status": "ok",
  "environment": "development",
  "timestamp": "2026-07-24T00:00:00+00:00",
  "ffmpeg_available": true,
  "ffmpeg_version": "7.1"
}
```

If FFmpeg is not installed or cannot be executed, the API remains available and returns:

```json
{
  "status": "ok",
  "environment": "development",
  "timestamp": "2026-07-24T00:00:00+00:00",
  "ffmpeg_available": false,
  "ffmpeg_version": null
}
```

## Project Structure

```text
app/
├── __init__.py
├── config.py
├── main.py
├── models.py
└── store.py

tests/
└── test_api.py

.github/
├── ISSUE_TEMPLATE/
└── workflows/
    └── ci.yml

Dockerfile
docker-compose.yml
requirements.txt
requirements-dev.txt
.env.example
CONTRIBUTING.md
LICENSE
README.md
```

## Local Development

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the application:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 3101
```

Run tests:

```bash
pytest -q
```

Run lint checks:

```bash
ruff check .
```

## Environment Variables

Copy `.env.example` to `.env` before starting the application.

Important variables include:

```env
APP_NAME=open-video-automation-toolkit
APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=3101

FFMPEG_PATH=ffmpeg
OUTPUT_DIR=./output
TEMP_DIR=./temp
```

Never commit the real `.env` file.

## Security

Never commit:

- API keys
- Passwords
- Access tokens
- OAuth refresh tokens
- Service-account credentials
- Private URLs
- Personal or customer information
- Production configuration files

Use environment variables for sensitive values.

Only placeholder values should be stored in `.env.example`.

## Project Status

The project is currently in early development.

Version `v0.1.0` provides:

- The initial FastAPI application
- Render job creation and status endpoints
- FFmpeg availability and version checks
- Docker configuration
- Automated tests
- GitHub Actions CI
- Contribution infrastructure

Planned development includes:

- Real FFmpeg video rendering
- Background job processing
- Subtitle generation
- Text-to-speech integrations
- n8n workflow examples
- YouTube publishing integration
- Google Drive archiving
- Telegram notifications

## Contributing

Contributions are welcome.

You can help by:

- Fixing bugs
- Improving documentation
- Adding tests
- Building new integrations
- Improving FFmpeg rendering features
- Creating n8n workflow examples

Start here:

- [Contribution Guide](CONTRIBUTING.md)
- [Open Issues](https://github.com/ekremshn/open-video-automation-toolkit/issues)
- [Good First Issues](https://github.com/ekremshn/open-video-automation-toolkit/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

Please comment on an issue before starting major work to avoid duplicate implementations.

## Release

The latest release is available here:

[Open Video Automation Toolkit v0.1.0](https://github.com/ekremshn/open-video-automation-toolkit/releases/tag/v0.1.0)

## License

This project is licensed under the [MIT License](LICENSE).
