import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar


class settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int
    database_url: str
    enable_docs: bool = True

    env: ClassVar[str] = os.getenv("ENVIRONMENT", "development")

    model_config: ClassVar[SettingsConfigDict]

    if env == "production":
        model_config = SettingsConfigDict(env_file=".env.production")
    else:
        model_config = SettingsConfigDict(env_file=".env.development")


settings = settings()
