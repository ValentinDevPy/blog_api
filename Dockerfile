FROM python:3.9-alpine3.14
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
WORKDIR /blog_api
COPY requirements.txt requirements.txt
RUN  pip3 install --upgrade pip && pip3 install -r requirements.txt && pip3 install psycopg2-binary