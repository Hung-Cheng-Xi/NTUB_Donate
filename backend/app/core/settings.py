import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar


class settings(BaseSettings):
    # App settings
    app_name: str
    admin_email: str
    items_per_user: int
    enable_docs: bool = True

    # API URLs
    barcode_api_url: str
    zipcode_api_url: str

    # PostgreSQL settings
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str
    google_client_id: str
    google_client_secret: str
    google_redirect_uri: str
    signing_key: str

    # FTP settings
    ftp_host: str
    ftp_port: int
    ftp_user: str
    ftp_password: str

    env: ClassVar[str] = os.getenv("ENVIRONMENT", "development")

    model_config: ClassVar[SettingsConfigDict]

    model_config = SettingsConfigDict(
        env_file=f".env.{env}"
    )


settings = Settings()
