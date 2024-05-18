from datetime import datetime

from schemas.basejason import BaseOrjsonModel


class Auth(BaseOrjsonModel):
    login: str
    login_time: datetime | str
