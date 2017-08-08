import json
from django.db.models import Count
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.filters import DjangoFilterBackend, OrderingFilter

from .serializers import UserCreationSerializer, UserDetailSerializer, UserCreationWithValidEmailSerializer
from .models import User
from .permissions import IsAccountOwner, IsAccountOwnerOrAdmin
from .clearbit_service import clearbit_enrichment


class UserReadOnlyViewSet(ReadOnlyModelViewSet):
    """
    A ViewSet for listing and retrieving users.
    """
    queryset = User.objects.annotate(posts_count=Count('posts')).all()
    serializer_class = UserDetailSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('posts_count',)
    # permission_classes = [AllowAny]


class UserUpdateDeleteViewSet(UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    A  ViewSet for updating and deleting users.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAccountOwnerOrAdmin]


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
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        email = request.query_params.get('email', None)
        if email:
            additional_user_data = clearbit_enrichment(email)       # TODO: replace it to serializer
            if additional_user_data:
                return Response(json.dumps(additional_user_data), status=status.HTTP_302_FOUND)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

