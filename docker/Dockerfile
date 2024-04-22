FROM python:3.11-slim

WORKDIR /app

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip install psycopg2-binary

RUN pip install -r requirements.txt

COPY main.py /app/main.py

COPY prothesis/ /app/prothesis
