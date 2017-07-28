from django.conf import settings
from django.db import models
from custom_user.models import AbstractEmailUser


class SocialNetworkUser(AbstractEmailUser):
    date_of_birth = models.DateField()
    avatar = models.CharField()
    bio = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
