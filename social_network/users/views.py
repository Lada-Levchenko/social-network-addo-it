import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from .serializers import UserCreationSerializer, UserDetailSerializer, UserCreationWithValidEmailSerializer
from .models import User
from .permissions import IsAccountOwner, IsAccountOwnerOrAdmin
from .clearbit_service import clearbit_enrichment


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
            additional_user_data = clearbit_enrichment(email)
            if additional_user_data:
                return Response(json.dumps(additional_user_data), status=status.HTTP_302_FOUND)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveView(RetrieveAPIView):
    """
    Get a single user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserUpdateView(UpdateAPIView):
    """
    Update an existing user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAccountOwnerOrAdmin]


class UserDeleteView(DestroyAPIView):
    """
    Delete an existing user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAccountOwnerOrAdmin]


class UserListView(ListAPIView):
    """
    Get a list of users by filters.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
