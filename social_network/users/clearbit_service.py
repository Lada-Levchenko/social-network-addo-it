#!/usr/bin/env python

import clearbit
from social_network_project.local_settings import CLEARBIT_API_KEY

clearbit.key = CLEARBIT_API_KEY


def clearbit_enrichment(email):
    lookup = clearbit.Person.find(email=email, stream=True)
    if lookup is not None:
        user = {
            'first_name': lookup['name']['givenName'],
            'last_name': lookup['name']['familyName'],
            'gender': lookup['gender'],
            'location': lookup['location'],
            'bio': lookup['bio'],
            'site': lookup['site'],
            'avatar': lookup['avatar']
        }
        return user
    return None
