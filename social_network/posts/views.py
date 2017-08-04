from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from .serializers import PostCreationSerializer, PostDetailSerializer, LikePostSerializer, UnlikePostSerializer
from .models import Post
from .permissions import IsAccountOwner, IsAccountOwnerOrAdmin


class PostCreateView(CreateAPIView):
    """
    Create a new post
    """
    serializer_class = PostCreationSerializer


class PostRetrieveView(RetrieveAPIView):
    """
    Get a single post.
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateView(UpdateAPIView):
    """
    Update an existing post.
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAccountOwnerOrAdmin]


class PostDeleteView(DestroyAPIView):
    """
    Delete an existing post.
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAccountOwnerOrAdmin]


class PostListView(ListAPIView):
    """
    Get a list of posts by author.
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_fields = ('author',)


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
