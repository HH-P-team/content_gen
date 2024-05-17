from http import HTTPStatus

from helpers.exceptions import AuthException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def password_validator(password):
    min_length = 8
    errors = []
    if len(password) < min_length:
        errors.append(
            AuthException(
                "Password must be at least 8 characters long",
                status_code=HTTPStatus.LENGTH_REQUIRED,
            )
        )

    if not any(character.islower() for character in password):
        errors.append(
            AuthException(
                "Password should contain at least one lowercase character",
                status_code=HTTPStatus.CONFLICT,
            )
        )

    if not any(character.isupper() for character in password):
        errors.append(
            AuthException(
                "Password should contain at least one upper character",
                status_code=HTTPStatus.CONFLICT,
            )
        )

    if errors:
        raise errors[0]

    return password
