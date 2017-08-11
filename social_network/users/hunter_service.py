import requests
from social_network_project.local_settings import HUNTER_API_KEY


class EmailHunter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_params = {'api_key': api_key}
        self.base_endpoint = 'https://api.hunter.io/v2/{}'

    def _query_hunter(self, endpoint, params, request_type='get', payload=None):
        if not payload:
            res = getattr(requests, request_type)(endpoint, params=params)
        else:
            res = getattr(requests, request_type)(endpoint, params=params, json=payload)
        res.raise_for_status()
        data = res.json()['data']
        return data

    def email_verifier(self, email):
        """
        Verify the deliverability of a given email
        :param email: The email address to check.
        :return: Full payload of the query as a dict.
        """
        params = {'email': email, 'api_key': self.api_key}
        endpoint = self.base_endpoint.format('email-verifier')
        return self._query_hunter(endpoint, params)

email_hunter = EmailHunter(HUNTER_API_KEY)
