FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/
WORKDIR /code/
ADD social_network/requirements.txt /code/social_network/
ADD automated_bot/requirements.txt /code/automated_bot/
ADD wait-for-it.sh /code/
RUN pip install gunicorn
RUN pip install -r social_network/requirements.txt
RUN pip install -r automated_bot/requirements.txt
ADD . /code/
RUN chmod +x /code/wait-for-it.sh
