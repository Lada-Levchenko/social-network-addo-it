import json
from django.db.models import Count
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import DjangoFilterBackend, OrderingFilter

from .serializers import UserCreationSerializer, UserDetailSerializer, UserCreationWithValidEmailSerializer, \
    UserAdditionalDataSerializer
from .models import User
from .permissions import IsAccountOwner, IsAccountOwnerOrAdminOrReadOnly, IsAccountOwnerOrAdminOrReadOnlyAuthenticated


class MyDjangoFilterBackend(DjangoFilterBackend):
    template = 'rest_framework/filters/django_filter.html'


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    A ViewSet for listing, retrieving, updating and deleting users.
    """
    queryset = User.objects.annotate(
        posts_count=Count('posts'),
        liked_posts_count=Count('liked_posts')
    ).all()
    serializer_class = UserDetailSerializer
    filter_backends = (OrderingFilter, MyDjangoFilterBackend)
    filter_fields = ('first_name', 'last_name', 'is_active')
    ordering_fields = ('posts_count', 'liked_posts_count')
    permission_classes = [IsAccountOwnerOrAdminOrReadOnly]  # can be changed to IsAccountOwnerOrAdminOrReadOnlyAuthenticated


class UserValidCreateView(CreateAPIView):
    """
    Register a new user performing an email validation.
    """
    serializer_class = UserCreationWithValidEmailSerializer
    permission_classes = [AllowAny]


class UserInvalidCreateView(CreateAPIView):
    """
    Register a new user without email validation (only for Admin).
    """
    serializer_class = UserCreationSerializer
    permission_classes = [IsAdminUser]


class UserAdditionalDataView(APIView):
    """
    Get an additional data for user by email.
    """
    serializer_class = UserAdditionalDataSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(data=request.query_params)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

