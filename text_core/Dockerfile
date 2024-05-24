FROM python:3.12.3

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip