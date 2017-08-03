from rest_framework import serializers

from .models import Post
from users.models import User
from users.serializers import UserMiniSerializer


class PostCreationSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        exclude = ('publication_time', 'users_liked')

    def validate_author(self, value):
        return self.context['request'].user


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer()

    class Meta:
        model = Post
        fields = ('author', 'text', 'publication_time', 'users_liked')

