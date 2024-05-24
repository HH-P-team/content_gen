import uuid
from datetime import datetime

from schemas.basejason import BaseOrjsonModel


class AccBase(BaseOrjsonModel):
    user_uuid: uuid.UUID
    login_time: datetime
