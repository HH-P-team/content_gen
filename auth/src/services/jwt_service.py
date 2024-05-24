import jwt

from core.settings import settings


class JwtService:

    algorithm = settings.jwt_algorithm
    secret_key = settings.jwt_secret_key

    def create_token(self, data: dict):
        token = jwt.encode(data, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_token(self, token: str):
        try:
            decoded_data = jwt.decode(
                token, self.secret_key, algorithms=[self.algorithm])
            return decoded_data
        except jwt.PyJWTError:
            return None
