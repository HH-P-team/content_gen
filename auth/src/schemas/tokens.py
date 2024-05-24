from pydantic import BaseModel, Field


class AccessToken(BaseModel):
    access_token: str = Field(title="access token")


class RefreshToken(BaseModel):
    refresh_token: str = Field(title="refresh token")
