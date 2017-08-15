#!/bin/bash

python social_network/manage.py makemigrations
python social_network/manage.py migrate --noinput
python social_network/manage.py initadmin

if  [[ $RUN_TYPE == "production" ]]; then
    gunicorn --chdir social_network social_network_project.wsgi -b 127.0.0.1:5000;
else
    python social_network/manage.py runserver 127.0.0.1:5000;
fi
