from sqlmodel import SQLModel


class AuthRequest(SQLModel):
    code: str


class AuthResponse(SQLModel):
    access_token: str


class GoogleTokenResponse(SQLModel):
    access_token: str
    expires_in: int
    scope: str
    token_type: str
    id_token: str

    class Config:
        from_attributes = True
