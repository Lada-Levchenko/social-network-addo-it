from django.db.models import Count
from rest_framework.generics import UpdateAPIView
from rest_framework.filters import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .serializers import PostDetailSerializer, LikePostSerializer, UnlikePostSerializer
from .models import Post
from .permissions import IsAccountOwner, IsAccountOwnerOrAdminOrReadOnly, IsAccountOwnerOrAdminOrReadOnlyAuthenticated


class PostViewSet(ModelViewSet):
    """
    A ViewSet for listing, retrieving, updating and deleting posts.
    """
    queryset = Post.objects.annotate(likes_count=Count('users_liked')).all()
    serializer_class = PostDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('likes_count',)
    permission_classes = [IsAccountOwnerOrAdminOrReadOnly]  # can be changed to IsAccountOwnerOrAdminOrReadOnlyAuthenticated


class LikePostView(UpdateAPIView):
    """
    Perform like as current user
    """
    queryset = Post.objects.all()
    serializer_class = LikePostSerializer


class UnlikePostView(UpdateAPIView):
    """
    Perform 'unlike' as current user
    """
    queryset = Post.objects.all()
    serializer_class = UnlikePostSerializer
