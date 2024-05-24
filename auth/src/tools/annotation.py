from typing import Annotated
from fastapi import Query, Body

from schemas import loginpass, tokens


class PaginationAnnotated:

    def __init__(
        self,
        page_number: Annotated[int, Query(
            description='page number', ge=0)] = 0,
        page_size: Annotated[int, Query(
            description='size of page', ge=1, le=100)] = 50,
    ):
        self.page_number = page_number
        self.page_size = page_size


class LoginPassAnnotated:
    def __init__(
        self,
        body: Annotated[
            loginpass.LoginPass,
            Body(
                examples=[
                    {
                        "login": "fern@nd@",
                        "password": "NiU(&9TR)",
                    }
                ],
            )
        ],

    ):
        self.body = body


class AccessTokenAnnotated:
    def __init__(
        self,
        body: Annotated[
            tokens.AccessToken,
            Body(
                examples=[
                    {
                        "access_token": "you access token",
                    }
                ],
            )
        ],

    ):
        self.body = body


class RefreshTokenAnnotated:
    def __init__(
        self,
        body: Annotated[
            tokens.RefreshToken,
            Body(
                examples=[
                    {
                        "refresh_token": "you refresh token",
                    }
                ],
            )
        ],

    ):
        self.body = body


class UpdatePassAnnotated:
    def __init__(
        self,
        body: Annotated[
            loginpass.UpdatePass,
            Body(
                examples=[
                    {
                        "login": "fern@nd@",
                        "password": "NiU(&9TR)",
                        "access_token": "you access token",
                    }
                ],
            )
        ],

    ):
        self.body = body


class UpdateAccAnnotated:
    def __init__(
        self,
        body: Annotated[
            loginpass.UpdateAcc,
            Body(
                examples=[
                    {
                        "login": "fern@nd@",
                        "password": "NiU(&9TR)",
                        "access_token": "you access token",
                    }
                ],
            )
        ],
    ):
        self.body = body
