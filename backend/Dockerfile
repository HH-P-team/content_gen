FROM python:3.10.12

RUN echo $API_PORT

RUN pip3 install pipenv

WORKDIR /opt/app

COPY ./Pipfile ./

RUN pipenv lock

RUN set -ex && pipenv install --deploy --system

COPY ./backend .

EXPOSE ${API_PORT}

CMD ["python", "start.py"]