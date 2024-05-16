from apscheduler.schedulers.blocking import BlockingScheduler
from sqlalchemy import select

from commons.db import get_db
from commons.models import Subject
from commons.neuro_gateway.mistral import Mistral
from commons.config import get_settings
from commons.utils import get_post_description

scheduler = BlockingScheduler()
settings = get_settings()
api = Mistral(settings.mistral_api_key)

# @scheduler.scheduled_job('interval', minutes=1)
def test_task() -> None:
    for db in get_db():
        stmt = select(Subject.name)
        for subject in db.scalars(stmt):
            print(subject)
            print(get_post_description(api, subject))

if __name__ == '__main__':
    test_task()