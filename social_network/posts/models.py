from django.db import models


class Post(models.Model):
    author = models.ForeignKey('users.User', related_name='posts')
    text = models.TextField()
    publication_time = models.DateTimeField(auto_now_add=True)
    users_liked = models.ManyToManyField('users.User', related_name='liked_posts')

    def liked_by(self, user_liked):
        if user_liked:
            self.users_liked.add(user_liked)
        return

    def unliked_by(self, user_unliked):
        if user_unliked:
            self.users_liked.remove(user_unliked)
        return
