FROM python:3

WORKDIR /app

ADD . /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app
