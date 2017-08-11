#!/bin/bash

python manage.py migrate --noinput
python manage.py initadmin

if  [[ $RUN_TYPE == "production" ]]; then
    gunicorn social_network_project.wsgi -b :5000;
else
    python manage.py runserver 0.0.0.0:8080;
fi
