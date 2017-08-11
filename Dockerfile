FROM python:3.6

ADD . /app

WORKDIR /app

RUN pip install gunicorn
RUN pip install -r social_network/requirements.txt
RUN pip install -r automated_bot/requirements.txt