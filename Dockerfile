FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD social_network/requirements.txt /code/social_network/
ADD automated_bot/requirements.txt /code/automated_bot/
RUN pip install -r social_network/requirements.txt
RUN pip install -r automated_bot/requirements.txt
ADD . /code/