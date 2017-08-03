from django.db import models


class Post(models.Model):
    author = models.ForeignKey('users.User', related_name='posts')
    text = models.TextField()
    publication_time = models.DateTimeField(auto_now_add=True)
    users_liked = models.ManyToManyField('users.User', related_name='liked_posts')

    def like(self, person_liked):
        if self.persons_liked.filter(id=person_liked).exists():
            self.persons_liked.add(person_liked)
        return

    def unlike(self, person_unliked):
        if self.persons_liked.filter(id=person_unliked).exists():
            self.persons_liked.remove(person_unliked)
        return
