from http import HTTPStatus

from pydantic import BaseModel, Field, validator

from helpers.exceptions import AuthException
from schemas.tokens import AccessToken
from services.password_service import password_validator


class Pass(BaseModel):
    password: str = Field(title="password")

    @validator('password', always=True)
    def validate_password(cls, value):
        value = password_validator(value)

        return value


class LoginPass(Pass):
    login: str = Field(title="login")

    @validator('login', always=True)
    def validate_login(cls, value):
        login = value
        min_length = 8
        errors = []
        if len(login) < min_length:
            errors.append(
                AuthException(
                    'Login must be at least 8 characters long',
                    status_code=HTTPStatus.LENGTH_REQUIRED,
                )
            )
        if errors:
            for error in errors:
                raise error

        return value


class UpdatePass(Pass, AccessToken):
    new_password: str = Field(title="new_password")

    @validator('new_password', always=True)
    def validate_new_password(cls, value):
        value = password_validator(value)


class UpdateAcc(LoginPass, AccessToken):
    pass
