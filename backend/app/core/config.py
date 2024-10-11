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

    # FTP settings
    ftp_host: str
    ftp_port: int
    ftp_user: str
    ftp_password: str

    env: ClassVar[str] = os.getenv("ENVIRONMENT", "development")

    model_config: ClassVar[SettingsConfigDict]

    if env == "production":
        model_config = SettingsConfigDict(env_file=".env.production")
    else:
        model_config = SettingsConfigDict(env_file=".env.development")


settings = settings()
