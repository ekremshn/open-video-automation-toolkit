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
- Automated tests
- GitHub Actions CI
- Issue and pull request templates

## Quick Start

```bash
git clone https://github.com/ekremshn/open-video-automation-toolkit.git
cd open-video-automation-toolkit
cp .env.example .env
docker compose up --build
```

Open:

- API: `http://localhost:3101`
- Swagger: `http://localhost:3101/docs`
- Health: `http://localhost:3101/health`

## Example Request

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

## Project Structure

```text
app/                 FastAPI application
tests/               Automated tests
.github/             GitHub templates and CI
output/              Generated videos
temp/                Temporary render files
Dockerfile           Container image
docker-compose.yml   Local orchestration
```

## Security

Never commit API keys, passwords, tokens, service-account files or private URLs.

Use `.env` locally and keep only placeholder values in `.env.example`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License.
