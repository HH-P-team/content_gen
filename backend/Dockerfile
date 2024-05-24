FROM python:3.10.12

RUN pip3 install pipenv

WORKDIR /opt/app

COPY ./Pipfile ./

RUN pipenv lock

RUN set -ex && pipenv install --deploy --system

# COPY ./backend .

EXPOSE ${API_PORT}

CMD ["python", "start.py"]