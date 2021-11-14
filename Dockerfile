FROM python:3.9-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache gcc libc-dev libffi-dev mariadb-dev

RUN pip install --upgrade pip && \
    pip install pipenv

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --dev --system

COPY . .
