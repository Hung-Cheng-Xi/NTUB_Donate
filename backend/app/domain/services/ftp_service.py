import paramiko
from fastapi import HTTPException

from app.core.settings import settings


class FTPService:
    def __init__(self):
        self.hostname = settings.ftp_host
        self.port = settings.ftp_port
        self.username = settings.ftp_user
        self.password = settings.ftp_password

    @property
    def session(self):
        if not hasattr(self, "_session"):
            self._session = self.connect()

        return self._session

    def connect(self):
        try:
            transport = paramiko.Transport((self.hostname, self.port))
            transport.connect(username=self.username, password=self.password)
            return paramiko.SFTPClient.from_transport(transport)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to connect to FTP server: {str(e)}"
            )

    def list_files(self, remote_path: str):
        try:
            return self.session.listdir(remote_path)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to list files: {str(e)}"
            )

    def refresh_data(self):
        pass

    def disconnect(self):
        self.session.close()
