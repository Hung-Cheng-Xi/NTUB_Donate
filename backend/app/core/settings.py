import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar


class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int
    enable_docs: bool = True
    barcode_api_url: str
    zipcode_api_url: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str
    google_client_id: str
    google_client_secret: str
    google_redirect_uri: str
    signing_key: str

    env: ClassVar[str] = os.getenv("ENVIRONMENT", "development")

    model_config: ClassVar[SettingsConfigDict]

    model_config = SettingsConfigDict(
        env_file=f".env.{env}"
    )


settings = Settings()
