from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserCreationSerializer, UserDetailSerializer
from .models import User


class UserCreateView(APIView):
    """
    Register a new user.
    """
    serializer_class = UserCreationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveView(RetrieveAPIView):
    """
    Get a single user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (AllowAny, )


class UserUpdateView(UpdateAPIView):        # TODO: PATCHing instead of PUTting
    """
    Update an existing user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (AllowAny,)        # TODO: change to IsAuthenticated


class UserDeleteView(DestroyAPIView):
    """
    Delete an existing user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (AllowAny,)        # TODO: change to IsOwner


class UserListView(ListAPIView):
    """
    Get a list of all users.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (AllowAny, )
    # authentication_classes = (JSONWebTokenAuthentication, )
