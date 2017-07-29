from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer


class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthLogin(APIView):
    """
     Manual implementation of login method
    """
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)
        # Generate token and add it to the response object
        if account is not None:
            login(request, account)
            return Response({
                'status': 'Successful',
                'message': 'You have successfully been logged into your account.'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'Unauthorized',
            'message': 'Username/password combination invalid.'
        }, status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'id': request.user.id,
            'username': request.user.username,
            'token': str(request.auth)
        }
        return Response(data)
