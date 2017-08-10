import random

import requests
import automated_bot.config as config
import json
from datetime import datetime
import names


class AutomatedBot(object):
    def __init__(self, api_url):
        self.api_url = api_url
        self.token = None
        self.headers = None
        self.users_emails = []
        self.session_password = config.admin_password
        file = open('sample.txt', 'r')
        self.sample_text_words = file.readline().split()
        file.close()

    def perform_login(self, data):
        response = requests.post(self.api_url + 'users/token-auth/', json=data)
        self.token = response.json()['token']
        self.headers = {'Authorization': 'JWT ' + self.token}
        return response.json()

    def perform_invalid_signup(self, data):
        response = requests.post(self.api_url + 'users/register-invalid/', json=data, headers=self.headers)
        return response.json()

    def get_additional_data_on_user(self, email):
        response = requests.get(self.api_url + 'users/additional-data/', params={'email': email}, headers=self.headers)
        return response.json()

    def perform_valid_signup(self, signup_data):
        additional_data = json.loads(self.get_additional_data_on_user(signup_data['email']))
        combined_signup_data = {
            'email': signup_data['email'],
            'password': signup_data['password'],
            'confirm_password': signup_data['confirm_password'],
            'first_name': additional_data['first_name'],
            'last_name': additional_data['last_name']
        }
        if additional_data['bio']:
            combined_signup_data['bio'] = additional_data['bio']
        if additional_data['avatar']:
            combined_signup_data['avatar'] = additional_data['avatar']
        response = requests.post(self.api_url + 'users/register/', json=combined_signup_data)
        return response.json()

    def get_users_list(self, params=None):
        response = requests.get(self.api_url + 'users/', params=params, headers=self.headers)
        return response.json()

    def create_post(self, data):
        response = requests.post(self.api_url + 'posts/', json=data, headers=self.headers)
        return response.json()

    def get_posts_list(self, params=None):
        response = requests.get(self.api_url + 'posts/', params=params, headers=self.headers)
        return response.json()

    def like_post(self, post_id):
        response = requests.put(self.api_url + 'posts/like/%s/' % post_id, headers=self.headers)
        return response.json()

    def generate_invalid_user(self, password):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        return {
            'email': '%s.%s.%s@gmail.com' % (first_name.lower(), last_name.lower(), str(datetime.now().microsecond)),
            'password': password,
            'confirm_password': password,
            'first_name': first_name,
            'last_name': last_name
        }

    def perform_invalid_signup_by_count(self, users_count):
        for user_number in range(0, users_count):
            user = self.generate_invalid_user(self.session_password)
            created_user = self.perform_invalid_signup(user)
            print(created_user)
            self.users_emails.append(created_user['email'])

    def generate_post(self):
        random_words_count = random.randint(1, 200)
        post = ' '.join(random.choice(self.sample_text_words) for _ in range(random_words_count))
        return post

    def create_posts_of_user(self, email, count):
        login_data = {
            'email': email,
            'password': self.session_password
        }
        self.perform_login(login_data)
        for index in range(count):
            post = {
                'text': self.generate_post()
            }
            self.create_post(post)

    def signup_and_create_posts_of_users(self, number_of_users, max_posts_per_user):
        self.perform_invalid_signup_by_count(number_of_users)
        for user_email in self.users_emails:
            posts_count = random.randint(1, max_posts_per_user)
            self.create_posts_of_user(user_email, posts_count)

    def run(self, number_of_users, max_posts_per_user, max_likes_per_user):
        login_data = {
            'email': config.admin_email,
            'password': config.admin_password
        }
        self.perform_login(login_data)
        self.signup_and_create_posts_of_users(number_of_users, max_posts_per_user)
        
        users_list_page = self.get_users_list({'ordering': '-posts_count'})
        extra_situation = False     # when only posts of current user are left with no likes
        while True:     # iterating over pages
            for user in users_list_page['results']:     # iterating over users on page
                if user['liked_posts_count'] == max_likes_per_user:
                    continue
                email = user['email']
                self.perform_login({'email': email, 'password': self.session_password})
                while user['liked_posts_count'] < max_likes_per_user:   # iterating over likes for user
                    random_user_id = user['id']
                    while random_user_id == user['id']:     # trying to spot another appropriate user to like his post
                        posts_with_no_likes = self.get_posts_list({'likes_count': '0'})
                        if posts_with_no_likes['count'] == 0:
                            return
                        posts_of_current_user_with_no_likes = sum(1 for post in posts_with_no_likes['results']
                                                                  if post['author'] == random_user_id)
                        if posts_of_current_user_with_no_likes == posts_with_no_likes['count']:
                            extra_situation = True
                            break
                        random_post = random.choice(posts_with_no_likes['results'])
                        random_user_id = random_post['author']
                    if extra_situation:
                        extra_situation = False
                        break
                    posts_of_random_user = self.get_posts_list({'author': random_user_id})
                    random_post = random.choice(posts_of_random_user['results'])
                    self.like_post(random_post['id'])
            if not users_list_page['next']:
                break
            response = requests.get(users_list_page['next'], headers=self.headers)
            users_list_page = json.loads(response.json())

bot = AutomatedBot(api_url=config.url)
bot.run(
    number_of_users=config.number_of_users,
    max_posts_per_user=config.max_posts_per_user,
    max_likes_per_user=config.max_likes_per_user
)
