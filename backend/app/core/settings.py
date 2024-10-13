import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar


class Settings(BaseSettings):
    """應用程式設定。

    Attributes:
        app_name (str): 應用程式名稱。
        admin_email (str): 管理員使用者的電子郵件地址。
        items_per_user (int): 每個使用者可以擁有的項目數量。
        enable_docs (bool): 是否啟用 API 文件。
        barcode_api_url (str): 條碼 API 的 URL。
        zipcode_api_url (str): 郵遞區號 API 的 URL。
        postgres_user (str): PostgreSQL 資料庫的使用者名稱。
        postgres_password (str): PostgreSQL 資料庫的密碼。
        postgres_host (str): PostgreSQL 資料庫的主機名稱。
        postgres_port (int): PostgreSQL 資料庫的連接埠。
        postgres_db (str): PostgreSQL 資料庫的名稱。
        google_client_id (str): Google OAuth 的客戶端 ID。
        google_client_secret (str): Google OAuth 的客戶端密鑰。
        google_redirect_uri (str): Google OAuth 的重新導向 URI。
        signing_key (str): 用於簽署 JWT 的密鑰。
        ftp_host (str): FTP 伺服器的主機名稱。
        ftp_port (int): FTP 伺服器的連接埠。
        ftp_user (str): FTP 伺服器的使用者名稱。
        ftp_password (str): FTP 伺服器的密碼。
        env (ClassVar[str]): 應用程式運行的環境。
        model_config (ClassVar[SettingsConfigDict]): 設定模型的配置。
    """
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
    google_redirect_url: str
    signing_key: str

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
