
from schemas.basejason import BaseOrjsonModel


class Auth(BaseOrjsonModel):
    login: str
    access_token: str
    refresh_token: str
    login_time: str
