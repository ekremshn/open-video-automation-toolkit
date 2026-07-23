from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "open-video-automation-toolkit"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 3101
    log_level: str = "INFO"

    ffmpeg_path: str = "ffmpeg"
    output_dir: Path = Path("./output")
    temp_dir: Path = Path("./temp")

    api_auth_token: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
