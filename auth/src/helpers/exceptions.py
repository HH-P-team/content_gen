from fastapi import HTTPException


class AuthException(HTTPException):
    def __init__(self, text, status_code):
        self.status_code = status_code
        self.detail = text
        self.txt = self.detail + f" http error {self.status_code}"
